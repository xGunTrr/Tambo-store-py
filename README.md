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
Por defecto el proyecto usa la url '127.0.0.1:5000/' pero contamos con más endpoints:
- `127.0.0.1:5000/signup`
Endpoint para el registro de usuarios.
- `127.0.0.1:5000/signin`
Endpoint para el logueo de usuarios.
- `127.0.0.1:5000/productos`
Endpoint que muestra las categorias, subcategorias y productos.
- `127.0.0.1:5000/usuarios`
Enpoint que muestra los roles y usuarios.
Como nos daremos cuenta, la aplicación nos enviará a la pestaña de login de forma automática en caso no estemos logueados, crearemos una cuenta para inciar con el uso yendo a `127.0.0.1:5000/signup`. 
