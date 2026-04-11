<h1 align="center">
  <br>
  Prizo ML
  <br>
</h1>

<h4 align="center">Scraper de alto rendimiento y herramienta de análisis de mercado para Mercado Libre.</h4>

<p align="center">
  <em>Leer en otros idiomas: <a href="README.md">Inglés</a>, <a href="README-es.md">Español</a></em>
</p>

<p align="center">
  <a href="#-características">Características</a> •
  <a href="#-cómo-funciona">Cómo Funciona</a> •
  <a href="#-instalación-y-uso">Instalación y Uso</a> •
  <a href="#-arquitectura">Arquitectura</a> •
  <a href="#-stack-tecnológico">Tech Stack</a>
</p>

---

> [!IMPORTANT]
> **Prizo ML** utiliza una tecnología exclusiva de "Fusión de Páginas" mediante una extensión de navegador para capturar cientos de productos en una sola pasada, superando los límites tradicionales de paginación.

**Prizo ML** es un ecosistema de scraping profesional diseñado para extraer, limpiar y analizar datos de productos de Mercado Libre en múltiples países de Latinoamérica. Al combinar la automatización de **Playwright** con una extensión de **JavaScript** personalizada, logra una recolección de datos ultrarrápida con lógica de deduplicación integrada.

Diseñado para investigadores de mercado y analistas de e-commerce, el proyecto garantiza la integridad de los datos mediante un algoritmo de "Huella Digital" que filtra anuncios patrocinados repetidos y variaciones de URLs de seguimiento.

---

## ✨ Características

- 🔗 **Fusión Inteligente de Páginas**: Extensión personalizada que fusiona hasta 20 páginas en un solo DOM para una extracción instantánea.
- 🛡️ **Deduplicación Inteligente**: Filtrado avanzado basado en la "huella" (Título + Precio) para eliminar anuncios redundantes y duplicados por parámetros de tracking.
- 📊 **Análisis de Mercado**: Escáner integrado potenciado por **Pandas** que calcula precios promedio, encuentra las mejores ofertas y exporta CSVs limpios.
- 🚀 **Lanzador en un Clic**: Incluye un archivo `.bat` para Windows que gestiona automáticamente la instalación de dependencias y la configuración del entorno.
- 🌎 **Soporte Multipaís**: Soporte nativo para AR, BR, MX, CO, CL y más de 13 regiones de Mercado Libre.

---

## 🚀 Cómo Funciona

Prizo ML utiliza una arquitectura híbrida para maximizar la eficiencia:

### 1. El Motor de Fusión (Lado del Navegador)
Un script de contenido en JavaScript detecta los resultados de búsqueda y realiza peticiones asíncronas de las páginas siguientes. Añade los nuevos ítems a la ventana activa, "engordando" el DOM antes de que el scraper comience.

### 2. El Núcleo de Extracción (Lado de Python)
Usando **Playwright**, el sistema lanza un contexto de navegador persistente con la extensión precargada. Espera a que el proceso de fusión termine y recolecta la lista completa de productos en una sola operación de milisegundos.

### 3. Sanitización de Datos
Cada producto pasa por una puerta de validación. Si la combinación única de Título y Precio ya ha sido procesada, el ítem se descarta, asegurando que el CSV final sea 100% único.

---

## 💻 Instalación y Uso

### Prerrequisitos
- [Python 3.10+](https://www.python.org/downloads/)
- Google Chrome instalado (recomendado)

### Pasos (La Vía Profesional)
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/SzntiDev/Prizo-ML.git
   cd prizo-ml
   ```
2. **Ejecutar el Lanzador Automático**:
   Simplemente haz doble clic en el archivo `run_Prizo_ML.bat`. 
   
   *Esto hará automáticamente:*
   - Crear el entorno de trabajo.
   - Instalar dependencias (`pip install -r requirements.txt`).
   - Configurar los motores de Playwright.
   - Iniciar el Scraper.
   - Generar las Estadísticas finales.

---

## 🏗️ Arquitectura

El proyecto sigue una estructura modular para facilitar su mantenimiento:

```text
prizo-ml/
├── extension_prizo/        # Extensión JS (Motor de Fusión)
│   ├── content.js          # Lógica central para unir páginas
│   └── manifest.json       # Configuración de la extensión
├── ml_scraper.py           # Script principal de automatización (Playwright)
├── ml_scanner.py           # Análisis de datos y estadísticas (Pandas)
├── run_Prizo_ML.bat        # Lanzador estandarizado (un solo clic)
├── requirements.txt        # Dependencias del proyecto
├── productos_ml.csv        # Salida de datos crudos/limpios
└── chrome_data/            # Sesiones persistentes del navegador
```

---

## ⚙️ Stack Tecnológico

- **[Python](https://www.python.org/)**: Lógica central y automatización.
- **[Playwright](https://playwright.dev/)**: Orquestación de navegador de alto nivel.
- **[Pandas](https://pandas.pydata.org/)**: Manipulación y análisis de datos.
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)**: Parseo preciso de HTML.
- **[JavaScript (ES6)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)**: Lógica de la extensión de navegador.

---
> Proyecto desarrollado con enfoque en la precisión de datos, velocidad de recolección y experiencia de usuario simplificada.
