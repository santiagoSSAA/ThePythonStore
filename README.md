# ThePythonStore: Tu Tienda Online Personalizada con Python

### Descripción
ThePythonStore es un proyecto de código abierto diseñado para enseñar los fundamentos del desarrollo web con Python y construir una tienda en línea funcional. Este proyecto te guiará a través de los conceptos clave del comercio electrónico, desde la creación de un catálogo de productos hasta la gestión de pedidos.

### Características Clave
* **Catálogo de productos:** Agrega, edita y elimina productos con facilidad.
* **Carrito de compras:** Permite a los usuarios agregar, eliminar y modificar productos en su carrito.
* **Proceso de pago simulado:** Simula un proceso de compra completo para una experiencia de usuario realista.
* **Panel de administración:** Gestiona tu tienda desde un panel de control intuitivo.
* **Escalable:** Diseñado para crecer contigo y adaptarse a tus necesidades.

### Tecnologías Utilizadas
* **[Python](https://www.python.org/)**.
* **[Django](https://www.djangoproject.com/)**.
* **[Django Rest Framework](https://www.django-rest-framework.org/)**
* **[PostgreSQL](https://www.postgresql.org/)**
* **[HTML](https://www.w3schools.com/html/), [CSS](https://www.w3schools.com/Css/) y [Javascript](https://www.w3schools.com/js/DEFAULT.asp)**
* **[Bootstrap](https://getbootstrap.com/)**

### Cómo Utilizar
1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/santiagoSSAA/ThePythonStore.git
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3.5. **Crea una base de datos PostgreSQL**
   - 3.5.1. Instala postgreSQL desde el link de arriba
   
   - 3.5.2. Crea una base de datos desde la terminal:
   ```bash
   psql
   CREATE DATABASE thepythonstore;
   \q
   ```

4. **Aplica las migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
Accede a `http://127.0.0.1:8000/` para ver tu tienda en línea.

6. Creando un superusuario (Opcional)
   ```bash
   python manage.py createsuperuser
   ```

6. Aplicando migraciones (Opcional)
   ```bash
   python manage.py makemigrations <insert-migration-name-here>
   python manage.py migrate
   ```

