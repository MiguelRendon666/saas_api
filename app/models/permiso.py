from app import db
from app.models.base import BaseObject

class Permiso(BaseObject):
    __tablename__ = 'permiso'
    
    nombre = db.Column(db.String(100), nullable=False)
    modulo = db.Column(db.String(100), nullable=False)
    crear = db.Column(db.Boolean, nullable=False, default=False)
    editar = db.Column(db.Boolean, nullable=False, default=False)
    desactivar = db.Column(db.Boolean, nullable=False, default=False)
    
    def __repr__(self):
        return f'<Permiso {self.nombre} - {self.modulo}>'
