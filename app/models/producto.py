from app import db
from app.models.base import BaseObject
from app.enums import UnidadMedida

class Producto(BaseObject):
    __tablename__ = 'producto'
    
    nombre = db.Column(db.String(200), nullable=False)
    unidadMedida = db.Column(db.Enum(UnidadMedida), nullable=False)
    
    # Foreign Key
    fkProveedorMarca = db.Column(db.String(36), db.ForeignKey('proveedor_marca.oid'), nullable=False)
    
    # Relaciones
    proveedorMarca = db.relationship('ProveedorMarca', back_populates='productos')
    
    def __repr__(self):
        return f'<Producto {self.nombre}>'
