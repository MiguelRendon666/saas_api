from app import db
from app.models.base import BaseObject

class ProveedorMarca(BaseObject):
    __tablename__ = 'proveedor_marca'
    
    nombre = db.Column(db.String(200), nullable=False)
    
    # Relaciones
    productos = db.relationship('Producto', back_populates='proveedorMarca')
    proveedor_productos = db.relationship('ProveedorProducto', back_populates='proveedor_marca')
    
    def __repr__(self):
        return f'<ProveedorMarca {self.nombre}>'
