from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/horarios")
def horarios():
    return render_template("horarios.html")

@app.route("/profesores")
def profesores():
    return render_template("profesores.html")

@app.route("/profesores/candela-pascual")
def candela():
    return render_template("profesores/candela.html")
@app.route("/profesores/nicolas-virulon")
def nicolas():
    return render_template("profesores/nicolas.html")
@app.route("/profesores/mariana-cagnelutti")
def mariana():
    return render_template("profesores/mariana.html")
@app.route("/profesores/emiliano-burgos")
def emiliano():
    return render_template("profesores/emiliano.html")
@app.route("/profesores/sergio-rosas")
def sergio():
    return render_template("profesores/sergio.html")

@app.route("/precios")
def precios():
    return render_template("precios.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)