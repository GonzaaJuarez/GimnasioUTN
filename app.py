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

@app.route("/precios")
def precios():
    return render_template("precios.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)