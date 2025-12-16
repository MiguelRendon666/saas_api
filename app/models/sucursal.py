from app import db
from app.models.base import BaseObject

class Sucursal(BaseObject):
    __tablename__ = 'sucursal'
    
    clave = db.Column(db.String(50), nullable=False, unique=True)
    nombre = db.Column(db.String(200), nullable=False)
    folio = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    
    # Foreign Key
    fkEmpresa = db.Column(db.String(36), db.ForeignKey('empresa.oid'), nullable=False)
    
    # Relaciones (1 sucursal tiene N usuarios)
    usuarios = db.relationship('Usuario', foreign_keys='Usuario.fkSucursal', back_populates='sucursal')
    empresa = db.relationship('Empresa', back_populates='sucursales', foreign_keys=[fkEmpresa])
    stock_sucursales = db.relationship('StockSucursal', back_populates='sucursal')
    lista_precios = db.relationship('ListaPrecios', back_populates='sucursal')
    
    def __repr__(self):
        return f'<Sucursal {self.nombre}>'
