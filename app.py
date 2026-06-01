from flask import Flask, render_template, request, redirect
from models import db, Profesor

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gimnasio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/horarios")
def horarios():
    return render_template("horarios.html")

@app.route("/profesores")
def profesores():
    lista_profesores = Profesor.query.all()
    return render_template(
        "profesores.html",
        profesores=lista_profesores
    )

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


@app.route("/admin")
def admin():
    return render_template("admin/index.html")
@app.route("/admin/profesores")
def admin_profesores():
    profesores = Profesor.query.all()
    return render_template(
        "admin/profesores.html",
        profesores=profesores
    )
@app.route("/admin/profesores/nuevo", methods=["GET", "POST"])
def nuevo_profesor():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        profesor = Profesor(
            nombre=nombre,
            telefono=telefono
        )
        db.session.add(profesor)
        db.session.commit()
        return redirect("/admin/profesores")
    return render_template("admin/nuevo_profesor.html")
@app.route("/admin/profesores/eliminar/<int:id>")
def eliminar_profesor(id):
    profesor = Profesor.query.get_or_404(id)
    db.session.delete(profesor)
    db.session.commit()
    return redirect("/admin/profesores")
@app.route("/admin/profesores/editar/<int:id>", methods=["GET", "POST"])
def editar_profesor(id):
    profesor = Profesor.query.get_or_404(id)
    if request.method == "POST":
        profesor.nombre = request.form["nombre"]
        profesor.telefono = request.form["telefono"]
        db.session.commit()
        return redirect("/admin/profesores")
    return render_template(
        "admin/editar_profesor.html",
        profesor=profesor
    )




with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)