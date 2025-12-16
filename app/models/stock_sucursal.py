from app import db
from app.models.base import BaseObject

class StockSucursal(BaseObject):
    __tablename__ = 'stock_sucursal'
    
    # Foreign Keys
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False, index=True)
    fkProducto = db.Column(db.String(36), db.ForeignKey('producto.oid'), nullable=False, index=True)
    
    # Atributos
    cantidad = db.Column(db.Integer, nullable=False, default=0)
    
    # Relaciones
    sucursal = db.relationship('Sucursal', back_populates='stock_sucursales')
    producto = db.relationship('Producto', back_populates='stock_sucursales')
    
    # Índices
    __table_args__ = (
        db.Index('ix_stock_sucursal_producto', 'fkSucursal', 'fkProducto', unique=True),
    )
    
    def __repr__(self):
        return f'<StockSucursal Sucursal:{self.fkSucursal} - Producto:{self.fkProducto} - Cantidad:{self.cantidad}>'
