console.log(`
===== Prizo ML =====                                                                        
`);


// funcion que busca productos y las pega

async function cargarMasPaginas(cantidad = 10) {
    let paginaActual = 1; // pagina actual

    while (paginaActual <= cantidad) {
        // Buscamos el link usando el atributo que encontraste en la captura
        const nextButton = document.querySelector('a[data-andes-pagination-control="next"]');

        if (!nextButton) {
            console.log("Ya no hay más páginas.");
            break;
        }
        const nextUrl = nextButton.href;
        console.log("Fusionando: " + nextUrl);
        // 1. Pedimos la página
        const respuesta = await fetch(nextUrl);
        const html = await respuesta.text();
        // 2. La procesamos
        const parser = new DOMParser();
        const docNueva = parser.parseFromString(html, 'text/html');
        // 3. Extraemos productos y los pegamos
        const nuevosProductos = docNueva.querySelectorAll('.ui-search-result__wrapper');
        const contenedor = document.querySelector('.ui-search-results');
        if (contenedor && nuevosProductos.length > 0) {
            nuevosProductos.forEach(prod => contenedor.appendChild(prod));

            // 4. Actualizamos el botón de la página actual con el de la nueva
            // para que en la siguiente vuelta del 'while' tengamos el link que sigue
            const nuevoBotonNext = docNueva.querySelector('a[data-andes-pagination-control="next"]');
            if (nuevoBotonNext) {
                nextButton.href = nuevoBotonNext.href;
            } else {
                nextButton.remove(); // Si no hay más, quitamos el botón
            }

            paginaActual++;
            console.log(`Página ${paginaActual} acoplada.`);
        } else {
            break;
        }
    }
    console.log("¡Fusión finalizada! Prizo tiene todos los datos listos.");
}
// No olvides llamar a la función al final
cargarMasPaginas(10);