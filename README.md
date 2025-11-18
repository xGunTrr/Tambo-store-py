# Tambo Store (proyecto personal)
Sistema de gestión de inventario para **Tiendas Tambo** haciendo uso de html, css y python.

## Requisitos
- python3.x
- Navegador web(google chrome, firefox, etc)
- pip o pip3

## Configurando el entorno
### Entorno Virtual
Crearemos un entorno virtual para aislas dependecias externas de nuestro sistema y evitar inconvenientes.

1. Creamos un entorno virtual
- Windows
```
python -m venv .venv
```
- Mac OS / Linux
```python
python3 -m venv .venv
```
2. Activamos el entorno virtual
- Windows
```
./.venv/bin/Script
```
- Mac OS / Linux
```
source .venv/bin/activate
```
3.  Descargamos los requerimientos
- Windows / Mac OS / Linux
```
pip install -r requirements.txt
```
### Instalación de requerimientos
## Modo de uso
Iniciaremos el servidor con el siguiente comando:
- Windows
```
python app.py
```
- Mac OS / Linux
```
python3 app/py
```
Podremos entrar a la app en la url por defecto `127.0.0.1:5000/`, en caso no estemos logueados se nos redirecciona a la página de login.
![Dashboard de la página](/static/img/examples/01-Dashboard.png)

- `127.0.0.1:5000/signup`
Endpoint para el registro de usuarios.
![Sign Up](/static/img/examples/02-Signup.png)

- `127.0.0.1:5000/signin`
Endpoint para el logueo de usuarios.
![Sign In](/static/img/examples/03-Signin.png)

- `127.0.0.1:5000/productos`
Endpoint que muestra las categorias, subcategorias y productos.
![Productos](/static/img/examples/04-productos.png)

- `127.0.0.1:5000/usuarios`
Enpoint que muestra los roles y usuarios.
![Usuarios](/static/img/examples/05-usuarios.png)
