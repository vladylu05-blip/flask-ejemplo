// Buscador de la tabla de estudiantes
const buscador = document.getElementById("buscador");
const tabla = document.getElementById("tabla-estudiantes");

if (buscador && tabla) {
    const filas = tabla.querySelectorAll("tbody tr");
    const sinResultados = document.getElementById("sin-resultados");

    buscador.addEventListener("input", () => {
        const texto = buscador.value.toLowerCase().trim();
        let visibles = 0;

        filas.forEach((fila) => {
            const coincide = fila.textContent.toLowerCase().includes(texto);
            fila.hidden = !coincide;
            if (coincide) visibles++;
        });

        if (sinResultados) sinResultados.hidden = visibles > 0;
    });
}

// Validación simple del formulario de contacto
const formulario = document.getElementById("form-contacto");

if (formulario) {
    const error = document.getElementById("error-formulario");

    formulario.addEventListener("submit", (evento) => {
        if (!formulario.checkValidity()) {
            evento.preventDefault();
            error.hidden = false;
        }
    });
}
