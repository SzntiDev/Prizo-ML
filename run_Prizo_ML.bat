@echo off
title Lanzador Prizo ML
cls

echo ==============
echo    PRIZO ML
echo ==============

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] No tienes Python instalado.
    echo Por favor, instala Python desde python.org y vuelve a intentarlo.
    pause
    exit
)

echo [1/3] Verificando e instalando librerias necesarias...
pip install -r requirements.txt

echo [2/3] Configurando motores de busqueda (Playwright)...
python -m playwright install chromium

echo [3/3] Iniciando Scraper de Mercado Libre...
python ml_scraper.py

echo.
echo ==========================================
echo    ANALIZANDO RESULTADOS FINALES...
echo ==========================================
python ml_scanner.py

echo.
echo ==========================================
echo    PROCESO COMPLETADO EXITOSAMENTE
echo ==========================================
pause
