from app import db
from app.models.base import BaseObject

class Rol(BaseObject):
    __tablename__ = 'rol'
    
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Rol {self.nombre}>'
