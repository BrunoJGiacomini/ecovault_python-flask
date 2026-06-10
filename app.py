from flask import Flask, render_template
from extensions import db
from repositories.usuario_repository import UsuarioRepository
from repositories.ecoponto_repository import EcopontoRepository
from repositories.descarte_repository import DescarteRepository
from models.usuario import Usuario
from models.ecoponto import Ecoponto
from models.descarte import Descarte
from controllers.descarte_controller import descarte_bp
from controllers.ecoponto_controller import ecoponto_bp
from controllers.usuario_controller import usuario_bp

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "ecovault-secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecovault.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(ecoponto_bp)
    app.register_blueprint(descarte_bp)

    @app.route("/")
    def index():
        total_usuarios = UsuarioRepository.total()

        total_ecopontos = EcopontoRepository.total()

        total_descartes = DescarteRepository.total()

        total_pontos = DescarteRepository.total_pontos()

        return render_template(
            "index.html",
            total_usuarios=total_usuarios,
            total_ecopontos=total_ecopontos,
            total_descartes=total_descartes,
            total_pontos=total_pontos
        )

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
