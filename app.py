from flask import Flask, render_template
from flask_login import LoginManager, login_required
from controller.forms_controller import form_bp
from controller.categorias_controller import categoria_bp
from controller.subcategorias_controller import subcategoria_bp
from controller.productos_controller import product_bp
from controller.usuarios_controller import user_bp
from controller.pedido_controller import pedidos_bp
from controller.registro_pedido_controller import registro_pedidos_bp
from model.usuario import Usuario

app = Flask(__name__)

app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'form_bp.signin'

# Controllers
app.register_blueprint(form_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(subcategoria_bp)
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)
app.register_blueprint(pedidos_bp)
app.register_blueprint(registro_pedidos_bp)



@app.route('/')
@login_required
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_user_by_id(user_id)

if __name__ == '__main__':
    app.run(debug=True)