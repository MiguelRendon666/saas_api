from app import db
from app.models.base import BaseObject
from datetime import datetime

class ListaPrecios(BaseObject):
    __tablename__ = 'lista_precios'
    
    # Foreign Keys
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False)
    fkProducto = db.Column(db.String(36), db.ForeignKey('producto.oid'), nullable=False)
    
    # Precios
    precioVenta = db.Column(db.Numeric(10, 2), nullable=False)
    precioCompra = db.Column(db.Numeric(10, 2), nullable=False)
    precioMayoreo = db.Column(db.Numeric(10, 2), nullable=True)
    precioPromocion = db.Column(db.Numeric(10, 2), nullable=True)
    vigenciaPromocion = db.Column(db.DateTime, nullable=True)
    
    # Relaciones
    sucursal = db.relationship('Sucursal', back_populates='lista_precios')
    producto = db.relationship('Producto', back_populates='lista_precios')
    
    def __repr__(self):
        return f'<ListaPrecios Sucursal:{self.fkSucursal} - Producto:{self.fkProducto} - Venta:{self.precioVenta}>'
