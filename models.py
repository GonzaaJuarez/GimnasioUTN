from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))

    def __repr__(self):
        return f"<Profesor {self.nombre}>"