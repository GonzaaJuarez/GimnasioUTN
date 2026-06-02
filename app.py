import os
import uuid
from flask import Flask, render_template, request, redirect
from models import db, Profesor, Horario
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
    horarios = Horario.query.all()
    return render_template(
        "horarios.html",
        horarios=horarios
    )

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
    return render_template("admin.html")
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

@app.route("/admin/horarios")
def admin_horarios():
    horarios = Horario.query.all()
    return render_template(
        "admin/horarios.html",
        horarios=horarios
    )
@app.route("/admin/horarios/nuevo", methods=["GET", "POST"])
def nuevo_horario():
    profesores = Profesor.query.all()
    if request.method == "POST":
        horario = Horario(
            dia=request.form["dia"],
            hora_inicio=request.form["hora_inicio"],
            hora_fin=request.form["hora_fin"],
            profesor_id=request.form["profesor_id"]
        )
        db.session.add(horario)
        db.session.commit()
        return redirect("/admin/horarios")
    return render_template(
        "admin/nuevo_horario.html",
        profesores=profesores
    )
@app.route("/admin/horarios/eliminar/<int:id>")
def eliminar_horario(id):
    horario = Horario.query.get_or_404(id)
    db.session.delete(horario)
    db.session.commit()
    return redirect("/admin/horarios")
@app.route(
    "/admin/horarios/editar/<int:id>",
    methods=["GET", "POST"]
)
def editar_horario(id):
    horario = Horario.query.get_or_404(id)
    profesores = Profesor.query.all()
    if request.method == "POST":
        horario.dia = request.form["dia"]
        horario.hora_inicio = request.form["hora_inicio"]
        horario.hora_fin = request.form["hora_fin"]
        horario.profesor_id = request.form["profesor_id"]
        db.session.commit()
        return redirect("/admin/horarios")
    return render_template(
        "admin/editar_horario.html",
        horario=horario,
        profesores=profesores
    )






with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)