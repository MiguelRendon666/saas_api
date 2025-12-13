from app import db
from app.models.base import BaseObject

class StockSucursal(BaseObject):
    __tablename__ = 'stock_sucursal'
    
    # Foreign Keys
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False)
    fkProducto = db.Column(db.String(36), db.ForeignKey('producto.oid'), nullable=False)
    
    # Atributos
    cantidad = db.Column(db.Integer, nullable=False, default=0)
    
    # Relaciones
    sucursal = db.relationship('Sucursal', back_populates='stock_sucursales')
    producto = db.relationship('Producto', back_populates='stock_sucursales')
    
    def __repr__(self):
        return f'<StockSucursal Sucursal:{self.fkSucursal} - Producto:{self.fkProducto} - Cantidad:{self.cantidad}>'
