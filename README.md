
# GimnasioUTN

Aplicación web para la gestión del gimnasio de la Universidad Tecnológica Nacional de la Facultad Regional de San Rafael (UTN-FRSR).

## Descripción

Este proyecto tiene como objetivo centralizar la información del gimnasio, permitiendo:

-   Consultar horarios de clases.
    
-   Visualizar precios según la categoría del alumno.
    
-   Consultar información de profesores.
    
-   Gestionar profesores, horarios y clases desde un panel administrativo.
    
-   Automatizar el cálculo de pagos a profesores y la distribución de ingresos.
    

Actualmente el proyecto se encuentra en desarrollo utilizando Python, Flask y SQLite.

## Tecnologías utilizadas

### Backend

-   Python 3.13
    
-   Flask 3.1.3

- Flask-SQLAlchemy
    
### Frontend

-   HTML5
    
-   CSS3
    
- Bootstrap 5

-   JavaScript
    

### Base de datos

-   SQLite (desarrollo)
    
-   PostgreSQL (planificado para producción)
    

### Control de versiones

-   Git
    
-   GitHub
    

## Estructura del proyecto

```text
GimnasioUTN/
│
├── app.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── instance/
│   └── gimnasio.db
│
├── static/
│   ├── css/
│   ├── js/
│   ├── uploads/
│   │   └── default.png
│
└── templates/
    │
    ├── admin.html
    ├── base.html
    ├── contacto.html
    ├── horarios.html
    ├── index.html
    ├── precios.html
    ├── profesor.html
    ├── profesores.html
    │
    └── admin/
        ├── editar_horario.html
        ├── editar_profesor.html
        ├── horarios.html
        ├── index.html
        ├── nuevo_horario.html
        ├── nuevo_profesor.html
        └── profesores.html

```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/GonzaaJuarez/GimnasioUTN.git
cd GimnasioUTN

```

### 2. Crear un entorno virtual

#### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

```

#### Windows (Git Bash)

```bash
python -m venv venv
source venv/Scripts/activate

```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt

```

### 4. Ejecutar la aplicación

```bash
python app.py

```

La aplicación estará disponible en:

```text
http://127.0.0.1:5000

```

## Estado actual

- Página principal
- Listado dinámico de profesores
- Ficha individual de profesor
- Subida de fotografías
- Imagen por defecto para profesores sin foto
- Panel administrativo
- CRUD completo de profesores
- CRUD completo de horarios
- Eliminación automática de horarios al eliminar un profesor
- Eliminación automática de imágenes al reemplazarlas o borrar profesores
- Horario semanal dinámico
- Visualización de horarios compartidos entre varios profesores
- Persistencia de datos mediante SQLite y SQLAlchemy

### Pendiente

- Validaciones de formularios
- Gestión de alumnos
- Gestión de cuotas
- Gestión de pagos a profesores
- Estadísticas e informes
- Migración a PostgreSQL
- Sistema de autenticación para administradores

---

## Autor

Desarrollado por Gonzalo Juarez y Gabriel Bruni como proyecto de práctica y aprendizaje de desarrollo web con Python y Flask.