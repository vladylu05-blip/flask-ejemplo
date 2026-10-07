from flask import Flask, render_template, request

app = Flask(__name__)

# Datos de ejemplo (más adelante pueden venir de una base de datos)
ESTUDIANTES = [
    {"id": 1, "nombre": "Ana Mamani", "carrera": "Ingeniería de Sistemas", "semestre": 5},
    {"id": 2, "nombre": "Carlos Quispe", "carrera": "Ingeniería de Sistemas", "semestre": 3},
    {"id": 3, "nombre": "Lucía Flores", "carrera": "Contaduría Pública", "semestre": 7},
    {"id": 4, "nombre": "Jorge Choque", "carrera": "Administración de Empresas", "semestre": 2},
    {"id": 5, "nombre": "María Condori", "carrera": "Ingeniería de Sistemas", "semestre": 8},
]


@app.route("/")
def inicio():
    return render_template(
        "inicio.html",
        titulo="Inicio",
        total_estudiantes=len(ESTUDIANTES),
    )


@app.route("/estudiantes")
def estudiantes():
    return render_template(
        "estudiantes.html",
        titulo="Estudiantes",
        estudiantes=ESTUDIANTES,
    )


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    enviado = False
    nombre = ""

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        enviado = True

    return render_template(
        "contacto.html",
        titulo="Contacto",
        enviado=enviado,
        nombre=nombre,
    )


if __name__ == "__main__":
    app.run(debug=True)
