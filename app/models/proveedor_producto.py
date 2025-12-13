from app import db
from app.models.base import BaseObject

class ProveedorProducto(BaseObject):
    __tablename__ = 'proveedor_producto'
    
    # Foreign Keys
    fkProveedorEmpleado = db.Column(db.String(36), db.ForeignKey('proveedor_empleado.oid'), nullable=False)
    fkProducto = db.Column(db.String(36), db.ForeignKey('producto.oid'), nullable=False)
    fkProveedorMarca = db.Column(db.String(36), db.ForeignKey('proveedor_marca.oid'), nullable=False)
    
    # Relaciones
    proveedor_empleado = db.relationship('ProveedorEmpleado', back_populates='proveedor_productos')
    producto = db.relationship('Producto', back_populates='proveedor_productos')
    proveedor_marca = db.relationship('ProveedorMarca', back_populates='proveedor_productos')
    
    def __repr__(self):
        return f'<ProveedorProducto Proveedor:{self.fkProveedorEmpleado} - Producto:{self.fkProducto} - Marca:{self.fkProveedorMarca}>'
