from app import db
from app.models.base import BaseObject
from app.enums import UnidadMedida

class Producto(BaseObject):
    __tablename__ = 'producto'
    
    clave = db.Column(db.String(50), nullable=False, unique=True)
    nombre = db.Column(db.String(200), nullable=False)
    codigo_barras = db.Column(db.String(100), nullable=True, unique=True)
    unidadMedida = db.Column(db.Enum(UnidadMedida), nullable=False)
    
    # Foreign Key
    fkProveedorMarca = db.Column(db.String(36), db.ForeignKey('proveedor_marca.oid'), nullable=False)
    
    # Relaciones
    proveedorMarca = db.relationship('ProveedorMarca', back_populates='productos')
    proveedor_productos = db.relationship('ProveedorProducto', back_populates='producto')
    stock_sucursales = db.relationship('StockSucursal', back_populates='producto')
    lista_precios = db.relationship('ListaPrecios', back_populates='producto')
    
    def __repr__(self):
        return f'<Producto {self.nombre}>'
