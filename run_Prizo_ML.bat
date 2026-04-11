@echo off
set CHROME_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
set EXTENSION_PATH="%CD%\extension_prizo"

echo Iniciando Chrome con Prizo Extension...
start "" %CHROME_PATH% --load-extension=%EXTENSION_PATH% "https://www.mercadolibre.com.ar"
