from app import db
from app.models.base_contacto import BaseContactoObject

class Empresa(BaseContactoObject):
    __tablename__ = 'empresa'
    
    clave = db.Column(db.String(50), nullable=False, unique=True, index=True)
    nombre = db.Column(db.String(200), nullable=False, index=True)
    folio = db.Column(db.String(100), nullable=False)
    urlLogo = db.Column(db.String(500), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    
    # Relaciones (1:1 con Usuario, 1:N con Sucursal)
    usuario = db.relationship('Usuario', foreign_keys='Usuario.fkEmpresa', back_populates='empresa', uselist=False)
    sucursales = db.relationship('Sucursal', back_populates='empresa', foreign_keys='Sucursal.fkEmpresa')
    
    def __repr__(self):
        return f'<Empresa {self.nombre}>'