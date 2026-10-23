# Gestión de Eventos con Django

Aplicación web desarrollada en **Django** para administrar eventos, registrar invitados y permitir la confirmación de asistencia mediante un número de cédula. Este proyecto fue desarrollado por **Santiago Restrepo González** como parte de las actividades académicas de Ingeniería de Software en el **Tecnológico de Antioquia**.

---

## Arquitectura del Proyecto

El sistema está diseñado bajo una arquitectura **feature-driven**, dividiendo el código por funcionalidades independientes y no por capas técnicas. Las dependencias fluyen en una sola dirección para mantener el código mantenible:

* **`core`**: Feature compartida que provee la plantilla base y los estilos globales CSS (*mobile-first*).
* **`eventos`**: Modelo principal, vistas públicas de lista/detalle y administración de los eventos.
* **`invitados`**: Modelo relacional con clave foránea a `Evento` para registrar las personas en la base de datos a través del panel de administración.
* **`confirmacion`**: Lógica de negocio mediante el patrón de servicios (`servicios.py`) para validar formularios y buscar invitaciones por cédula.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu máquina:
* **Python**: Versión `3.10` o superior.
* **Pip**: Gestor de paquetes de Python.

---

## Instalación y Despliegue Local

Por buenas prácticas de seguridad y control de versiones, la carpeta del entorno virtual (`.venv`) y la base de datos local (`db.sqlite3`) están excluidas del repositorio y deben ser recreadas en tu máquina local.

### 1. Clonar el repositorio
Ejecuta el siguiente comando en tu terminal para descargar el código fuente:
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd event_management
```

### 2. Crear el entorno virtual
Crea un entorno aislado para las librerías del proyecto ejecutando:
* **En Windows:**
  ```bash
  python -m venv .venv
  ```
  *(o usa `py -m venv .venv`)*
* **En Linux/macOS:**
  ```bash
  python3 -m venv .venv
  ```

### 3. Activar el entorno virtual
* **En Windows (cmd):**
  ```cmd
  .venv\Scripts\activate
  ```
* **En Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **En Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```

### 4. Instalar las dependencias
Una vez activado el entorno, instala la versión específica de Django (`>5.2, <5.3`):
```bash
pip install -r requirements.txt
```

### 5. Configurar la base de datos
Ejecuta las migraciones para crear las tablas físicas a partir de los modelos de Python:
```bash
python manage.py migrate
```

### 6. Crear el administrador
Genera las credenciales de acceso para el panel administrativo web:
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
Inicia el servidor local de desarrollo:
```bash
python manage.py runserver
```

---

### Accesos Locales

Cuando el servidor esté corriendo, puedes ingresar a las siguientes direcciones en tu navegador:
* **Aplicación Web:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Panel de Administración:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

