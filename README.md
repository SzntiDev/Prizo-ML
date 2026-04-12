# Prizo-ML

A specialized Machine Learning-ready dataset generator and scraper for Mercado Libre, focusing on market analysis and price tracking.

## Description
Prizo-ML is a Python-based utility part of the Prizo ecosystem, designed to collect high-quality product data from Mercado Libre. It automates the extraction of titles, prices, and links, saving the results in both CSV and Excel formats for further analysis or training machine learning models.

## Detailed Overview
Understanding market trends requires large amounts of data. Prizo-ML addresses this by scraping hundreds of product results from search queries. It includes a specialized scanner module that can verify product availability and price changes over time. The tool is designed to mimic human-like browsing patterns to ensure reliable data collection without triggering anti-scraping measures.

## Features
- Mass scraping of products from Mercado Libre
- Concurrent scanning and data validation
- Data export to structured `productos_ml.csv` and `productos_ml.xlsx`
- Custom Chrome profile integration for persistent sessions
- Intelligent filtering of sponsored or irrelevant results
- Pre-processing logic for machine learning dataset preparation

## Technologies Used
- Python 3.x
- Selenium / Playwright (Web automation)
- Pandas (Excel and CSV processing)
- Openpyxl (Advanced Excel formatting)

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/SzntiDev/Prizo-ML.git
   ```
2. Navigate to the project directory:
   ```bash
   cd prizo-ml
   ```
3. Install dependencies:
   ```bash
   pip install selenium pandas openpyxl
   ```
4. (Optional) Configure your Chrome data path in the script.

## Usage Examples
To start scraping products:
```bash
python ml_scraper.py
```
To run the price scanner on saved products:
```bash
python ml_scanner.py
```

## Project Structure
- `ml_scraper.py`: Primary engine for extracting product data.
- `ml_scanner.py`: Module for periodic price updates and availability checks.
- `productos_ml.csv`: Raw data storage.
- `productos_ml.xlsx`: Formatted report for human review.
- `run_Prizo_ML.bat`: Quick-start batch file for Windows.
- `chrome_data/`: Local cache for browser sessions.
- `extension_prizo/`: Core browser extension components (if applicable).

## Configuration
Modify the `requirements.txt` if additional libraries are needed. You can adjust the scraping delay and result limit in `ml_scraper.py`.

## API Documentation
Internal logic is documented via Python docstrings.

## Screenshots or Examples
![Scraped Data Example](productos_ml.xlsx) *(Example of the generated Excel report)*

## Roadmap / Future Improvements
- Price prediction models using regression
- Real-time alerts for price drops
- Support for other e-commerce platforms (Amazon, eBay)
- Web dashboard for data visualization

## Contributing Guidelines
Contributions are welcome. Please ensure any new features included unit tests for the scraper logic.

## License
MIT License

---

# Prizo-ML (Español)

Un generador de conjuntos de datos y extractor especializado para Mercado Libre, enfocado en el análisis de mercado y seguimiento de precios.

## Descripción
Prizo-ML es una utilidad basada en Python diseñada para recopilar datos de productos de alta calidad de Mercado Libre. Automatiza la extracción de títulos, precios y enlaces, guardando los resultados en formatos CSV y Excel para su posterior análisis o entrenamiento de modelos de IA.

## Resumen Detallado
Comprender las tendencias del mercado requiere grandes cantidades de datos. Prizo-ML aborda esto extrayendo cientos de resultados de productos. Incluye un módulo de escaneo especializado que puede verificar la disponibilidad de productos y los cambios de precios a lo largo del tiempo.

## Características
- Extracción masiva de productos de Mercado Libre
- Escaneo concurrente y validación de datos
- Exportación de datos a `productos_ml.csv` y `productos_ml.xlsx`
- Integración con perfiles de Chrome personalizados
- Filtrado inteligente de resultados patrocinados
- Lógica de preprocesamiento para preparación de datasets de ML

## Tecnologías Utilizadas
- Python 3.x
- Selenium / Playwright
- Pandas / Openpyxl

## Instrucciones de Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/SzntiDev/Prizo-ML.git
   ```
2. Navegar al directorio `prizo-ml`.
3. Instalar dependencias:
   ```bash
   pip install selenium pandas openpyxl
   ```
4. Ejecutar el extractor:
   ```bash
   python ml_scraper.py
   ```

## Estructura del Proyecto
- `ml_scraper.py`: Motor principal de extracción.
- `ml_scanner.py`: Módulo para actualizaciones periódicas.
- `productos_ml.csv`: Almacenamiento de datos crudos.
- `run_Prizo_ML.bat`: Archivo para ejecución rápida.

## Guía para Contribuir
¡Las contribuciones son bienvenidas!

## Licencia
Licencia MIT
