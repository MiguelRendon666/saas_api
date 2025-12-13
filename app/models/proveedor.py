from app import db
from app.models.base import BaseObject
from app.models.base_contacto import BaseContactoObject

class ProveedorMarca(BaseObject):
    __tablename__ = 'proveedor_marca'
    
    nombre = db.Column(db.String(200), nullable=False)
    
    # Relaciones
    productos = db.relationship('Producto', back_populates='proveedorMarca')
    
    def __repr__(self):
        return f'<ProveedorMarca {self.nombre}>'

class ProveedorEmpleado(BaseContactoObject):
    __tablename__ = 'proveedor_empleado'
    
    apellidoPaterno = db.Column(db.String(100), nullable=False)
    apellidoMaterno = db.Column(db.String(100), nullable=False)
    nombres = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f'<ProveedorEmpleado {self.nombres} {self.apellidoPaterno}>'
