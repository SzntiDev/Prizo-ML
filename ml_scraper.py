import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import os
async def main():
    print("\nScraper Mercado Libre")
    
    async with async_playwright() as p:
        ruta_extension = os.path.abspath("./extension_prizo")
        user_data_dir = os.path.abspath("./chrome_data")

        contexto = await p.chromium.launch_persistent_context(
            user_data_dir,
            headless=False,  #sin modo oculto asi si se ven las extensiones
            args=[
                f"--disable-extensions-except={ruta_extension}",
                f"--load-extension={ruta_extension}",
            ],
        )
        
        pagina = contexto.pages[0] if contexto.pages else await contexto.new_page()
        
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
        
        dominio = DOMINIOS.get(codpais, "com")

        alworks = []
        url_actual = f"https://listado.mercadolibre.{dominio}/{producto}"
            
        print(f"Buscando productos en: {url_actual}")
        await pagina.goto(url_actual)
        
        print("""
 ____                                         __               
/\  _`\        __                     /'\_/`\/\ \              
\ \ \L\ \_ __ /\_\  ____     ___     /\      \ \ \             
 \ \ ,__/\`'__\/\ \/\_ ,`\  / __`\   \ \ \__\ \ \ \  __        
  \ \ \/\ \ \/ \ \ \/_/  /_/\ \L\ \   \ \ \_/\ \ \ \L\ \       
   \ \_\ \ \_\  \ \_\/\____\ \____/    \ \_\  \ \_\ \____/       
    \/_/  \/_/   \/_/\/____/\/___/      \/_/   \/_/\/___/        
                                                               
                                                               
La extensión está fusionando las páginas... espera 15 segundos.
        """)
        await pagina.wait_for_timeout(15000) 
            
        html = await pagina.content()
        sopa = BeautifulSoup(html, "html.parser")
        alworks = sopa.find_all("div", class_="ui-search-result__wrapper")
        
        # Diccionario para los resultados
        price_link = {} 

    
        print(f"\n¡Genial! Encontré {len(alworks)} posibles productos para analizar.")

        lista_final = []
        num_a_procesar = len(alworks) 
        
        print(f"Ahora voy a extraer el detalle de los primeros {num_a_procesar} productos...")
        vistos = set()
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
                huella = (titulo, precio)                

                # Guardamos en el diccionario
                price_link[url_detalle] = precio
                
                print(f"[{i+1}/{num_a_procesar}] Encontrado: {titulo[:40]}... -> ${precio}")
                if huella not in vistos:
                    vistos.add(huella)
                    lista_final.append({
                        "Título": titulo,
                        "Link": url_detalle,
                        "Precio": precio
                    })

        if lista_final:
            df = pd.DataFrame(lista_final)
            df.to_csv("productos_ml.csv", index=False, encoding="utf-8-sig")
            print(f"\n¡Listo! Ya guardé toda la información en 'productos_ml.csv'.")
        
        await contexto.close()

if __name__ == "__main__":
    asyncio.run(main())
