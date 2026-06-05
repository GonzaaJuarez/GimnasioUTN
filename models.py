from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(120))
    instagram = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    foto = db.Column(db.String(255))

    horarios = db.relationship(
        "Horario",
        backref="profesor",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Profesor {self.nombre}>"
    
class Horario(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    dia = db.Column(db.String(20), nullable=False)

    hora_inicio = db.Column(db.String(5), nullable=False)
    hora_fin = db.Column(db.String(5), nullable=False)

    profesor_id = db.Column(
        db.Integer,
        db.ForeignKey("profesor.id"),
        nullable=False
    )