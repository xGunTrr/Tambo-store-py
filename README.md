# Tambo Store
## Requerimientos
- python 3.x
- sqlite3 (viene por defecto como librería estándar en python)
- tkinter (generalmente viene por defecto como librería en python)
- pip o pip3 (para instalación de librerías externas a través de PIP)
## Descargar las dependencias
1. Creamos un entorno virtual
- Windows
```cmd
python -m venv .venv
```
- Linux
```bash
python3 -m venv .venv
```
2. Activamos el entorno virtual
- Windows
```cmd
.venv/Scripts/activate
```
- Linux
```bash
source .venv/bin/activate
```
3. Descargamos las dependecias
```
pip install -r requirements.txt
```
## Cómo ejecutar el proyecto
- Windows
```cmd
python main.py
```
- Linux
```bash
python3 main.py
```
> [!IMPORTANT]
> Para poder realizar los siguientes pasos, te debes encontrar en la ruta raiz del proyecto.
## Cómo subir mis cambios al repositorio
Cuando te sientas seguro de que un cambio es realmente significativo en el código, significa que está listo para subirse al repositorio.
1. Añadimos los archivos al repositorio local
- Añadir por archivo
```bash
git add <nombre_de_archivo>
```
- Añadir todos los archivos (no se añadirán los del .gitignore)
```bash
git add .
```
2. Realizamos un commit en donde se especifique en pocas palabras lo realizado
```bash
git commit -m "<mensaje>"
```
3. Subimos los cambios al repositorio en la nube(github)
```bash
git push origin main
```
## Cómo actualizar el repositorio en mi máquina local
En caso algún usuario haga actualizaciones y quieres que se vean reflejadas en tu máquina, usa este comando en git bash (Windows) o Terminal (Linux).
```bash
git pull origin main
```