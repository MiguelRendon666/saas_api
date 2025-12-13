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
        from app.models import (
            base, empresa, usuario, rol, 
            permiso, sucursal, proveedor, producto
        )
    
    return app
