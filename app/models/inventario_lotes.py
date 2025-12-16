from app import db
from app.models.base import BaseObject

class InventarioLotes(BaseObject):
    __tablename__ = 'inventario_lotes'
    
    # Foreign Keys
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False, index=True)
    fkProducto = db.Column(db.String(36), db.ForeignKey('producto.oid'), nullable=False, index=True)
    
    # Atributos
    cantidad = db.Column(db.Integer, nullable=False, default=0)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Relaciones
    sucursal = db.relationship('Sucursal', back_populates='inventario_lotes')
    producto = db.relationship('Producto', back_populates='inventario_lotes')
    
    # Índices
    __table_args__ = (
        db.Index('ix_inventario_lotes_sucursal_producto', 'fkSucursal', 'fkProducto'),
    )
    
    def __repr__(self):
        return f'<InventarioLotes Sucursal:{self.fkSucursal} - Producto:{self.fkProducto} - Cantidad:{self.cantidad} - Precio:{self.precio}>'
