import os
import uuid
from flask import Flask, render_template, request, redirect
from models import db, Profesor
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/uploads"

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

@app.route("/profesores/<int:id>")
def detalle_profesor(id):
    profesor = Profesor.query.get_or_404(id)
    return render_template(
        "profesor.html",
        profesor=profesor
    )

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
        email = request.form["email"]
        instagram = request.form["instagram"]
        descripcion = request.form["descripcion"]
        archivo = request.files["foto"]
        nombre_archivo = None
        if archivo and archivo.filename:
            extension = os.path.splitext(
                archivo.filename
            )[1]
            nombre_archivo = (
                str(uuid.uuid4()) + extension
            )
            archivo.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    nombre_archivo
                )
            )
        profesor = Profesor(
            nombre=nombre,
            telefono=telefono,
            email=email,
            instagram=instagram,
            descripcion=descripcion,
            foto=nombre_archivo
        )
        db.session.add(profesor)
        db.session.commit()
        return redirect("/admin/profesores")
    return render_template("admin/nuevo_profesor.html")
@app.route("/admin/profesores/eliminar/<int:id>")
def eliminar_profesor(id):
    profesor = Profesor.query.get_or_404(id)
    if profesor.foto:
        ruta_foto = os.path.join(
            app.config["UPLOAD_FOLDER"],
            profesor.foto
        )
        if os.path.exists(ruta_foto):
            os.remove(ruta_foto)
    db.session.delete(profesor)
    db.session.commit()
    return redirect("/admin/profesores")
@app.route("/admin/profesores/editar/<int:id>", methods=["GET", "POST"])
def editar_profesor(id):
    profesor = Profesor.query.get_or_404(id)
    if request.method == "POST":
        profesor.nombre = request.form["nombre"]
        profesor.telefono = request.form["telefono"]
        profesor.email = request.form["email"]
        profesor.instagram = request.form["instagram"]
        profesor.descripcion = request.form["descripcion"]

        eliminar_foto = request.form.get("eliminar_foto")
        if eliminar_foto and profesor.foto:
            ruta_foto = os.path.join(
                app.config["UPLOAD_FOLDER"],
                profesor.foto
            )
            if os.path.exists(ruta_foto):
                os.remove(ruta_foto)
            profesor.foto = None

        archivo = request.files["foto"]
        if archivo and archivo.filename:
            # borrar foto anterior
            if profesor.foto:
                ruta_vieja = os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    profesor.foto
                )
                if os.path.exists(ruta_vieja):
                    os.remove(ruta_vieja)
            # generar nombre único
            import uuid
            extension = os.path.splitext(
                archivo.filename
            )[1]
            nombre_archivo = (
                str(uuid.uuid4()) + extension
            )
            archivo.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    nombre_archivo
                )
            )
            profesor.foto = nombre_archivo
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