from app import db
from app.models.base import BaseObject

class Sucursal(BaseObject):
    __tablename__ = 'sucursal'
    
    clave = db.Column(db.String(50), nullable=False, unique=True, index=True)
    nombre = db.Column(db.String(200), nullable=False, index=True)
    folio = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    
    # Foreign Key - referencia a empresa en otro microservicio
    fkEmpresa = db.Column(db.String(36), nullable=False, index=True)
    
    # Relaciones
    turnos = db.relationship('TurnoSucursal', back_populates='sucursal')
    cortes_caja = db.relationship('CorteCaja', back_populates='sucursal')
    
    def __repr__(self):
        return f'<Sucursal {self.nombre}>'
