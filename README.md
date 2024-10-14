Este es un proyecto básico de un CRM construido con Django.

## Requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.x
- Django (ver instrucciones de instalación abajo)
- Un entorno virtual para aislar las dependencias del proyecto

## Instrucciones de instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/crm-django-main.git
   ```

2. **Accede al directorio del proyecto**:
   ```bash
   cd crm-django-main/crm-django-main
   ```

3. **Crea un entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv env
   ```

4. **Activa el entorno virtual**:
   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - En Windows:
     ```bash
     .\env\Scripts\activate
     ```

5. **Instala las dependencias**:
   Asegúrate de que `pip` esté actualizado y luego instala las dependencias del proyecto:
   ```bash
   pip install django django-crispy-forms crispy-bootstrap5
   ```

6. **Configura la base de datos**:
   El proyecto usa una base de datos SQLite por defecto.
   Aplica las migraciones necesarias para crear las tablas en la base de datos:
   ```bash
   python manage.py migrate
   ```

7. **Crea un superusuario** (opcional, para acceder al panel de administración de Django):
   ```bash
   python manage.py createsuperuser
   ```

8. **Ejecuta el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

   Luego, abre tu navegador y visita: `http://127.0.0.1:8000/`.

## Archivos más relevantes

- **manage.py**: Archivo principal para ejecutar comandos de Django.
- **crm-django-main/djcrm/settings.py**: Archivo de configuración principal del proyecto (configura la base de datos, aplicaciones instaladas, etc.).
- **crm-django-main/djcrm/urls.py**: Define las rutas principales del proyecto.
- **crm-django-main/website/models.py**: Define los modelos utilizados en la aplicación CRM.
- **crm-django-main/website/views.py**: Contiene la lógica de las vistas que gestionan las solicitudes de los usuarios.
- **crm-django-main/website/templates/**: Contiene las plantillas HTML que renderizan las vistas.
- **crm-django-main/website/forms.py**: Define los formularios utilizados para crear y editar clientes.

## Estructura del Proyecto

```
crm-django-main/
│
├── crm-django-main/
│   ├── djcrm/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── website/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   └── manage.py
└── ...
```

## Funcionalidades del Proyecto

- Crear, actualizar y eliminar clientes desde el CRM.
- Iniciar y cerrar sesión.
- Ver detalles de clientes individuales.
