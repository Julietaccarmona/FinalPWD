# 🌎 Observatorio de Cooperación Internacional Subnacional

## Descripción

El **Observatorio de Cooperación Internacional Subnacional** es una aplicación web desarrollada como Trabajo Práctico Integrador de la asignatura **Programación Web Dinámica**.

Su objetivo es registrar, consultar y gestionar convenios de cooperación internacional celebrados entre gobiernos subnacionales, organismos públicos, universidades y otros actores, constituyendo una base de datos colaborativa sobre iniciativas de paradiplomacia.

---

## Objetivos del proyecto

* Implementar una arquitectura cliente-servidor.
* Desarrollar una API REST utilizando Flask.
* Consumir la API desde una aplicación Vue.js.
* Implementar autenticación mediante JSON Web Tokens (JWT).
* Gestionar permisos mediante roles de usuario.
* Aplicar buenas prácticas de organización del código utilizando el patrón MVC.

---

## Tecnologías utilizadas

### Frontend

* Vue 3
* Vue Router
* Pinia
* Axios

### Backend

* Python
* Flask
* Flask-JWT-Extended
* Flask-SQLAlchemy
* Flask-Migrate

### Base de datos

* PostgreSQL

---

## Arquitectura

El proyecto está dividido en dos aplicaciones independientes:

```
Frontend (Vue)
        │
      Axios
        │
 API REST (Flask)
        │
 SQLAlchemy
        │
 PostgreSQL
```

El backend implementa una API REST protegida mediante JWT, mientras que el frontend consume dichos servicios utilizando Axios.

---

## Funcionalidades implementadas

### Autenticación

* Registro de usuarios.
* Inicio de sesión.
* Generación de Access Token.
* Generación de Refresh Token.
* Renovación automática del Access Token.
* Protección de rutas mediante JWT.
* Cierre de sesión.

### Gestión de convenios

* Listado de convenios.
* Alta de nuevos convenios.
* Edición de convenios.
* Eliminación de convenios.

### Seguridad

* Usuarios autenticados pueden consultar la información.
* Cualquier usuario autenticado puede crear convenios.
* Cada usuario únicamente puede editar los convenios que creó.
* El administrador puede editar cualquier convenio.
* Solo el administrador puede eliminar convenios.

---

## Modelo de datos

La aplicación trabaja con las siguientes entidades principales:

* Usuarios
* Convenios
* Países
* Actores
* Tipos de convenio

Cada convenio registra:

* Título
* Descripción
* Fecha de firma
* Estado
* País
* Actor
* Tipo de convenio
* Usuario que realizó la carga

---

## Usuarios de prueba

### Administrador

* Rol: Administrador

Permisos:

* Crear convenios
* Editar cualquier convenio
* Eliminar convenios

### Usuario estándar

* Rol: Usuario

Permisos:

* Crear convenios
* Editar únicamente los convenios propios

---

## Estructura del proyecto

```
frontend/
    src/
        components/
        router/
        services/
        stores/
        views/

backend/
    app/
        controllers/
        models/
        routes/
        services/
        utils/
```

---

## Cómo ejecutar el proyecto

### Backend

```bash
cd backend

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python3 run.py
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Funcionalidades futuras

Como evolución del proyecto se prevé incorporar:

* Aprobación de convenios por parte del administrador antes de su publicación.
* Buscador de convenios.
* Filtros por país, actor y tipo.
* Panel de administración.
* Estadísticas y visualizaciones.
* Carga de documentos asociados a cada convenio.
* Diseño responsive para dispositivos móviles.

---

## Autora

**Julieta Cecilia Carmona**
 

## Licencia

Proyecto desarrollado con fines exclusivamente académicos.
