import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def main():
    print("\nScraper Mercado Libre")
    
    async with async_playwright() as p:
        navegador = await p.chromium.launch(headless=False)
        pagina = await navegador.new_page()
        
        while True:
            mensaje_pais = """
   Primero, dime en qué país quieres que busque:
   - ar (Argentina)   - br (Brasil)      - mx (México)
   - co (Colombia)    - cl (Chile)       - pe (Perú)
   - uy (Uruguay)     - ve (Venezuela)   - ec (Ecuador)
   - bo (Bolivia)     - py (Paraguay)    - cr (Costa Rica)
   - pa (Panamá)      - do (Rep. Dom)    - gt (Guatemala)
   - hn (Honduras)    - sv (El Salvador) - ni (Nicaragua)
   Tu respuesta: """
            codpais = input(mensaje_pais).strip().lower()
            if codpais in ["ar", "br", "mx", "co", "cl", "pe", "uy", "ve", "ec", "bo", "py", "cr", "pa", "do", "gt", "hn", "sv", "ni"]:
                break
            print("\nUps, ese código no lo reconozco. ¿Podrías intentar de nuevo?")

        producto = input("\n¿Qué tipo de producto te gustaría analizar?: ").replace(" ", "-").lower().strip()
        productoalt = producto.replace("-", "%20")


        while True:
            t_input = input("\n¿Cuántos segundos quieres que espere entre páginas? (Si no sabes, dale Enter y yo me encargo): ").strip()
            if t_input == "":
                wait_time = 2000
                break
            if t_input.replace(",", ".").replace(".", "", 1).isdigit():
                wait_time = int(float(t_input.replace(",", ".")) * 1000)
                break
            print("\nPerdón, necesito que sea un número para saber cuánto esperar.")

        DOMINIOS = {
            "ar": "com.ar", "br": "com.br", "mx": "com.mx", "co": "com.co",
            "cl": "cl", "pe": "com.pe", "uy": "com.uy", "ve": "com.ve",
            "ec": "com.ec", "bo": "com.bo", "py": "com.py", "cr": "co.cr",
            "pa": "com.pa", "do": "com.do", "gt": "com.gt", "hn": "com.hn",
            "sv": "com.sv", "ni": "com.ni"
        }
        
        # Obtenemos el dominio correcto según el código que ingresó el usuario
        # Si no existe, usamos "com" por defecto
        dominio = DOMINIOS.get(codpais, "com")

        alworks = []
        for npag in range(1, 4):
            desde = (npag - 1) * 48 + 1
            
            if npag == 1:
                url_actual = f"https://listado.mercadolibre.{dominio}/{producto}"
            else:
                url_actual = f"https://listado.mercadolibre.{dominio}/{producto}_Desde_{desde}"
            
            print(f"Buscando en Página {npag}...")
            await pagina.goto(url_actual)
            await pagina.wait_for_timeout(wait_time)
            
            html = await pagina.content()
            sopa = BeautifulSoup(html, "html.parser")
            productos_pagina = sopa.find_all("div", class_="ui-search-result__wrapper")
            
            # Usamos .extend() para sumar lo nuevo a lo que ya teníamos
            alworks.extend(productos_pagina)

        price_link = {} #diccionario para guardar el precio y el link

        # for npag in range(1, 6):
        url_actual = f"https://listado.mercadolibre.com.{codpais}/{producto}#D[A:{productoalt}]"
            # if npag > 1:
            #     url_actual += f"?p={npag}"
            
        print(f"Buscando productos en: {url_actual}")
        await pagina.goto(url_actual)
        await pagina.wait_for_timeout(wait_time)
            
        html = await pagina.content()
        sopa = BeautifulSoup(html, "html.parser")


        
        productos = sopa.find_all("div", class_="ui-search-result__wrapper")
        alworks.extend(productos)

        print(f"\n¡Genial! Encontré {len(alworks)} posibles productos para analizar.")

        lista_final = []
        num_a_procesar = len(alworks) 
        
        print(f"Ahora voy a extraer el detalle de los primeros {num_a_procesar} productos...")
        
        for i, tarjeta in enumerate(alworks[:num_a_procesar]):
            titulo_elem = tarjeta.find("h2", class_="poly-component__title")
            if not titulo_elem:
                titulo_elem = tarjeta.find("h3", class_="poly-component__title-wrapper")
            
            # 2. Buscamos el Link (es el link dentro del título)
            link_elem = titulo_elem.find("a") if titulo_elem else None
            
            # 3. Buscamos el Precio
            precio_elem = tarjeta.find("span", class_="andes-money-amount__fraction")
            
            if link_elem and precio_elem:
                url_detalle = link_elem['href']
                # Si el link es relativo (empieza con /), le ponemos el dominio
                if url_detalle.startswith("/"):
                    url_detalle = f"https://www.mercadolibre.{dominio}" + url_detalle
                
                titulo = titulo_elem.text.strip()
                precio = precio_elem.text.strip()
                
                # Guardamos en el diccionario
                price_link[url_detalle] = precio
                
                print(f"[{i+1}/{num_a_procesar}] Encontrado: {titulo[:40]}... -> ${precio}")
                
                lista_final.append({
                    "Título": titulo,
                    "Link": url_detalle,
                    "Precio": precio
                })

        if lista_final:
            df = pd.DataFrame(lista_final)
            df.to_csv("productos_ml.csv", index=False, encoding="utf-8-sig")
            print(f"\n¡Listo! Ya guardé toda la información en 'productos_ml.csv'.")
        
        await navegador.close()

if __name__ == "__main__":
    asyncio.run(main())
