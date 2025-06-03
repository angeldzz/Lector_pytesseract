from PIL import Image
import pytesseract
import re
import json
import os
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def normalize_amount(value: Optional[str]) -> Optional[float]:
    if not value:
        return None
    try:
        cleaned = re.sub(r'[^\d.,]', '', value).replace(',', '.').strip()
        if cleaned:
            return float(cleaned)
        return None
    except (ValueError, TypeError):
        logging.warning(f"Could not convert amount to float: {value}")
        return None

def normalize_date(date_str: Optional[str]) -> Optional[str]:
    if not date_str:
        return None
    match = re.match(r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})', date_str)
    if match:
        day, month, year = match.groups()
        year = year if len(year) == 4 else f"20{year.zfill(2)}"
        return f"{int(day):02d}/{int(month):02d}/{year}"
    logging.warning(f"Invalid date format: {date_str}")
    return None

def extract_emails(texto: str) -> List[str]:
    email_pattern = r'([a-zA-Z0-9._+-]+[a-zA-Z0-9-]*[a-zA-Z0-9._+-]?@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    potential_emails = re.findall(r'([a-zA-Z0-9._+-]+(?:Q|G)?[a-zA-Z0-9._+-]?[a-zA-Z0-9-]*(?:\.[a-zA-Z0-9-.]+))', texto)
    
    emails = []
    for email in potential_emails:
        normalized = email.replace('Q', '@').replace('G', '@').replace('O', '0')
        if re.match(email_pattern, normalized):
            emails.append(normalized)
    return emails if emails else None

def extract_data_from_text(texto: str) -> Dict:
    patterns = {
        "fecha": [r'Fecha\s*(?:de\s*factura)?[:\-]?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})'],
        "numero_factura": [r'Factura\s*(?:Recapitulativa)?\s*#?([A-Z0-9/\-]+)', r'N[úu]mero\s*de\s*factura[:\-]?\s*([A-Z0-9/\-]+)'],
        "base_imponible": [r'BASE\s*IMPONIBLE[:\s]*([\d.,]+)\s*€?', r'Total\s*Base\s*Imponible[:\s]*([\d.,]+)\s*€?'],
        "iva": [r'IVA\s*\(?(\d{1,2}(?:[.,]\d+)?)%?\)?\s*[:\-]?\s*([\d.,]+)\s*€?', r'IVA\s*[:\-]?\s*([\d.,]+)\s*€?', r'INA\s*(\d{1,2}%)?\s*[:\-]?\s*([\d.,]+)\s*€?'],
        "re": [r'R\.?E\.?\s*(?:\(\s*[\d.,]+%?\s*\))?\s*[:\-]?\s*([\d.,]+)\s*€?'],
        "total": [r'TOTAL\s*[:\-]?\s*([\d.,]+)\s*€', r'bbl\s*([\d.,]+)\s*€'],
        "cif": [r'CIF[:\s/]*([A-Z0-9]+)', r'CIF/NIF[:\s/]*([A-Z0-9]+)'],
        "nif": [r'NIF[:\s/]*([A-Z0-9]+)'],
        "cp_ciudad": r'(\d{5}),\s*([^\n,]+)'
    }

    datos = {
        "Fecha": None,
        "NumeroFactura": None,
        "BaseImponible": None,
        "IVA": None,
        "IVA_Porcentaje": None,
        "RE": None,
        "Total": None,
        "CIF": None,
        "NIF": None,
        "Emails": None,
        "CP_Ciudad": None
    }

    for key, pattern_list in patterns.items():
        for pattern in pattern_list if isinstance(pattern_list, list) else [pattern_list]:
            match = re.search(pattern, texto, re.IGNORECASE)
            if match:
                if key == "fecha":
                    datos["Fecha"] = normalize_date(match.group(1))
                elif key == "numero_factura":
                    datos["NumeroFactura"] = match.group(1).strip()
                elif key == "base_imponible":
                    datos["BaseImponible"] = normalize_amount(match.group(1))
                elif key == "iva":
                    if len(match.groups()) >= 2:
                        # Use normalize_amount to handle the percentage (strip %)
                        percentage = normalize_amount(match.group(1))
                        datos["IVA_Porcentaje"] = percentage if percentage is not None else None
                        datos["IVA"] = normalize_amount(match.group(2))
                    else:
                        datos["IVA"] = normalize_amount(match.group(1))
                elif key == "re":
                    datos["RE"] = normalize_amount(match.group(1))
                elif key == "total":
                    datos["Total"] = normalize_amount(match.group(1))
                elif key == "cif":
                    datos["CIF"] = match.group(1).strip()
                elif key == "nif":
                    datos["NIF"] = match.group(1).strip()
                break

    datos["Emails"] = extract_emails(texto)
    cp_ciudad = re.findall(patterns["cp_ciudad"], texto)
    datos["CP_Ciudad"] = [f"{cp[0]}, {cp[1].strip()}" for cp in cp_ciudad] if cp_ciudad else None

    return datos

def process_invoice_image(ruta_imagen: str) -> Dict:
    try:
        imagen = Image.open(ruta_imagen)
        imagen = imagen.convert('L')
        texto = pytesseract.image_to_string(imagen, lang='spa')
        logging.info("Text extracted successfully")
        print("Texto extraído:")
        print(texto)
        datos = extract_data_from_text(texto)
        return datos
    except Exception as e:
        logging.error(f"Error processing image {ruta_imagen}: {str(e)}")
        raise

def save_to_json(datos: Dict, json_file: str = "datos_extraidos.json") -> None:
    try:
        if os.path.exists(json_file) and os.stat(json_file).st_size > 0:
            with open(json_file, "r", encoding="utf-8") as f:
                datos_lista = json.load(f)
                if not isinstance(datos_lista, list):
                    datos_lista = []
        else:
            datos_lista = []

        datos_lista.append(datos)

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(datos_lista, f, ensure_ascii=False, indent=4)

        logging.info(f"Data saved to {json_file}")
        print("JSON generado:")
        print(json.dumps(datos, ensure_ascii=False, indent=4))
    except Exception as e:
        logging.error(f"Error saving to JSON: {str(e)}")
        raise

def main():
    ruta_imagen = "imagenes/Factura3.png"
    datos = process_invoice_image(ruta_imagen)
    save_to_json(datos)

if __name__ == "__main__":
    main()