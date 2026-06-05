from models import Horario
import re


def horario_superpuesto(
    dia,
    hora_inicio,
    hora_fin,
    horario_id=None
):
    horarios = Horario.query.filter_by(
        dia=dia
    ).all()

    for horario in horarios:

        # ignorar el propio horario al editar
        if (
            horario_id is not None
            and horario.id == horario_id
        ):
            continue

        # permitir horarios exactamente iguales
        if (
            horario.hora_inicio == hora_inicio
            and horario.hora_fin == hora_fin
        ):
            continue

        # detectar superposición
        if (
            hora_inicio < horario.hora_fin
            and hora_fin > horario.hora_inicio
        ):
            return True

    return False

def horario_valido(
    hora_inicio,
    hora_fin
):
    return hora_inicio < hora_fin

def nombre_valido(nombre):
    return bool(nombre.strip())
def telefono_valido(telefono):
    if not telefono:
        return True

    patron = r"^[0-9+\-\s]+$"
    return bool(re.match(patron, telefono))
def email_valido(email):
    if not email:
        return True

    patron = r"^[^@]+@[^@]+\.[^@]+$"
    return bool(re.match(patron, email))
