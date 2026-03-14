from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Importar modelos para que SQLAlchemy los registre
    with app.app_context():
        from app import models
    
    # Registrar blueprints
    from app.routes import usuario_bp, rol_bp, permiso_bp, permiso_asignado_bp, usuario_rol_bp
    app.register_blueprint(usuario_bp)
    app.register_blueprint(rol_bp)
    app.register_blueprint(permiso_bp)
    app.register_blueprint(permiso_asignado_bp)
    app.register_blueprint(usuario_rol_bp)
    
    return app
