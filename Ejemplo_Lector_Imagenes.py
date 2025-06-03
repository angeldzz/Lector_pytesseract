from PIL import Image
import pytesseract

# Configurar la ruta de Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta de la imagen
ruta_imagen = "imagenes/ejemploFactura.webp"

# Abrir la imagen
imagen = Image.open(ruta_imagen)

# Extraer el texto usando pytesseract
texto = pytesseract.image_to_string(imagen, lang='spa')  # Usa 'eng' para inglés, 'spa' para español

print("Texto extraído:")
print(texto)