console.log(`
===== Prizo ML =====                                                                        
`);


// funcion que busca productos y las pega
async function cargarMasPaginas(cantidad = 20) {
    let paginaActual = 1;

    // 1. LIMPIEZA TOTAL: Quitamos #, ?, y cualquier _Desde_ previo
    let urlBase = window.location.href
        .split('#')[0]          // Corta el # rebelde
        .split('?')[0]          // Corta los filtros ?
        .split(/_Desde_\d+/)[0]; // Corta el _Desde_ anterior

    // Quitamos la barra final / si existe
    if (urlBase.endsWith('/')) urlBase = urlBase.slice(0, -1);

    while (paginaActual <= cantidad) {
        // 2. Calculamos el salto de 48 en 48
        let desde = 1 + (paginaActual * 48);

        // 3. Montamos la URL perfecta
        const nextUrl = `${urlBase}_Desde_${desde}_NoIndex_True`;
        console.log("Fusionando página " + (paginaActual + 1) + ": " + nextUrl);

        try {
            const respuesta = await fetch(nextUrl);
            const html = await respuesta.text();
            const parser = new DOMParser();
            const docNueva = parser.parseFromString(html, 'text/html');

            const nuevosProductos = docNueva.querySelectorAll('.ui-search-result__wrapper');
            const contenedor = document.querySelector('.ui-search-results');

            if (contenedor && nuevosProductos.length > 0) {
                nuevosProductos.forEach(prod => contenedor.appendChild(prod));
                console.log(`¡Éxito! Página acoplada desde el ítem ${desde}.`);
                paginaActual++;
            } else {
                console.log("Ya no hay más productos únicos.");
                break;
            }
        } catch (error) {
            console.error("Error al pedir página:", error);
            break;
        }
    }
    console.log("--- PROCESO TERMINADO ---");
}

cargarMasPaginas(20);
