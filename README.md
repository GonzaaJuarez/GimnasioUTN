
# GimnasioUTN

Aplicación web para la gestión del gimnasio de la Universidad Tecnológica Nacional de la Facultad Regional de San Rafael (UTN-FRSR).

## Descripción

Este proyecto tiene como objetivo centralizar la información del gimnasio, permitiendo:

-   Consultar horarios de clases.
    
-   Visualizar precios según la categoría del alumno.
    
-   Consultar información de profesores.
    
-   Gestionar profesores, horarios y clases desde un panel administrativo.
    
-   Automatizar el cálculo de pagos a profesores y la distribución de ingresos.
    

Actualmente el proyecto se encuentra en una etapa inicial de desarrollo utilizando Python y Flask.

## Tecnologías utilizadas

### Backend

-   Python 3.13
    
-   Flask 3.1.3
    

### Frontend

-   HTML5
    
-   CSS3
    
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
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│
├── static/
│   ├── css/
│   └── js/
│
└── templates/

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

-   Configuración inicial del proyecto
    
-   Integración con GitHub
    
-   Entorno virtual configurado
    
-   Aplicación Flask funcional
    
-   Gestión de profesores
    
-   Gestión de horarios
    
-   Gestión de precios
    
-   Gestión de alumnos
    
-   Cálculo automático de pagos
    
-   Panel administrativo
    

## Autor

Desarrollado por Gonzalo Ariel Juárez como proyecto de práctica y aprendizaje de desarrollo web con Python y Flask.