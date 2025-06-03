# 🧾 Invoice OCR Extractor 

> **Transforma facturas escaneadas en datos estructurados con un solo click** 📸➡️📊

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![Tesseract](https://img.shields.io/badge/Tesseract-OCR-green.svg)](https://github.com/tesseract-ocr/tesseract)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

## 🎯 **¿Qué hace este proyecto?**

Convierte automáticamente **facturas en imagen** en **datos JSON estructurados** usando inteligencia artificial OCR. ¡Olvídate de escribir datos manualmente!

### ✨ **Antes y Después**

```
📄 FACTURA.PNG  ➜  🔍 OCR MAGIC  ➜  📊 JSON ESTRUCTURADO
```

## 🚀 **Características Principales**

### 📋 **Datos Extraídos Automáticamente**
- 📅 **Fecha de factura** - Formato normalizado DD/MM/YYYY
- 🔢 **Número de factura** - Identificador único
- 💰 **Base imponible** - Cantidad sin impuestos
- 🏛️ **IVA** - Importe y porcentaje automático
- 📈 **Recargo de Equivalencia (RE)** 
- 💵 **Total de factura**
- 🏢 **CIF/NIF** - Identificación fiscal
- 📧 **Emails** - Direcciones de contacto
- 🏙️ **Código Postal y Ciudad**

### 🛠️ **Tecnologías de Vanguardia**
- 🤖 **OCR con Tesseract** - Reconocimiento óptico de caracteres
- 🐍 **Python 3.13** - Última versión estable
- 🔍 **Regex Avanzadas** - Patrones inteligentes de extracción
- 📝 **Logging Profesional** - Seguimiento completo del proceso
- 🎨 **Normalización Automática** - Fechas y cantidades perfectas

## 📊 **Ejemplo de Salida JSON**

```json
{
  "Fecha": "26/09/2019",
  "NumeroFactura": "4F190006", 
  "BaseImponible": 423.97,
  "IVA": 89.03,
  "IVA_Porcentaje": 21.0,
  "RE": null,
  "Total": 513.0,
  "CIF": "A12345678",
  "NIF": null,
  "Emails": ["facturacion@empresa.com"],
  "CP_Ciudad": ["28001, Madrid"]
}
```

## 🏗️ **Estructura del Proyecto**

```
📁 JPG_JSON_PDF/
├── 🖼️ imagenes/
│   └── Factura3.png
├── 📊 Include/
├── 📚 Lib/
├── ⚙️ Scripts/
├── 🎯 Avance_IMG-JSON.py
├── 📄 datos_extraidos.json
├── 📝 Ejemplo_Lector_Imagenes.py
└── ⚡ pyvenv.cfg
```

## 🚀 **Instalación Rápida**

### 1️⃣ **Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/invoice-ocr-extractor.git
cd invoice-ocr-extractor
```

### 2️⃣ **Instala Tesseract OCR**
- **Windows**: [Descargar Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- **macOS**: `brew install tesseract`
- **Linux**: `sudo apt-get install tesseract-ocr`

### 3️⃣ **Instala dependencias Python**
```bash
pip install pytesseract pillow
```

### 4️⃣ **Configura la ruta de Tesseract**
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## 🎮 **Uso Súper Fácil**

### 🖱️ **Ejecución Básica**
```bash
python Avance_IMG-JSON.py
```

### 🔧 **Personalización Avanzada**
```python
# Procesar una factura específica
ruta_imagen = "imagenes/mi_factura.png"
datos = process_invoice_image(ruta_imagen)
save_to_json(datos, "mi_archivo.json")
```

## 🎨 **Características Técnicas Avanzadas**

### 🧠 **Algoritmos Inteligentes**
- **Normalización de cantidades**: Maneja comas, puntos y símbolos
- **Validación de fechas**: Formatos flexibles DD/MM/YY o DD/MM/YYYY  
- **Detección de emails**: Incluso con caracteres OCR mal leídos
- **Patrones regex multicapa**: Múltiples intentos de extracción

### 🔍 **Procesamiento de Imagen**
- Conversión automática a escala de grises
- Optimización para OCR en español
- Manejo de errores robusto
- Logging detallado del proceso

### 💾 **Gestión de Datos**
- Guardado incremental en JSON
- Preservación de datos existentes
- Encoding UTF-8 para caracteres especiales
- Estructura de datos consistente

## 📈 **Casos de Uso**

- 🏢 **Empresas**: Automatizar contabilidad
- 🏪 **Comercios**: Digitalizar facturas de proveedores  
- 👨‍💼 **Freelancers**: Organizar gastos empresariales
- 📊 **Contadores**: Procesar lotes de facturas
- 🤖 **Integraciones**: APIs de facturación automática

## 🛡️ **Manejo de Errores**

El sistema incluye logging profesional que registra:
- ✅ Éxitos en extracción de texto
- ⚠️ Advertencias en normalización de datos
- ❌ Errores en procesamiento de imagen
- 📋 Estado completo del proceso

## 🎯 **Próximas Funcionalidades**

- [ ] 🖼️ Soporte para múltiples formatos (PDF, TIFF, etc.)
- [ ] 🌐 API REST para integración web
- [ ] 📱 Interfaz gráfica de usuario
- [ ] 🔄 Procesamiento por lotes
- [ ] 🎯 Machine Learning para mejor precisión
- [ ] 🌍 Soporte multiidioma

## 🤝 **Contribuciones**

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea tu rama de funcionalidad (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 **Licencia**

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 **Agradecimientos**

- **Tesseract OCR** - Por hacer posible el reconocimiento de texto
- **Python Community** - Por las increíbles bibliotecas
- **Contributors** - Por hacer este proyecto mejor cada día

---

<div align="center">

### 🌟 **¡Dale una estrella si te gusta el proyecto!** ⭐

[![GitHub stars](https://img.shields.io/github/stars/tu-usuario/invoice-ocr-extractor.svg?style=social&label=Star)](https://github.com/tu-usuario/invoice-ocr-extractor)
[![GitHub forks](https://img.shields.io/github/forks/tu-usuario/invoice-ocr-extractor.svg?style=social&label=Fork)](https://github.com/tu-usuario/invoice-ocr-extractor/fork)

**Hecho con ❤️ en España 🇪🇸**

</div>
