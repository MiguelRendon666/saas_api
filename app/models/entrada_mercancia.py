from app import db
from app.models.base import BaseObject

class EntradaMercancia(BaseObject):
    __tablename__ = 'entrada_mercancia'
    
    fecha = db.Column(db.DateTime, nullable=False)
    costo_subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    descuento = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    costo_total = db.Column(db.Numeric(10, 2), nullable=False)
    observaciones = db.Column(db.Text, nullable=True)
    
    # Foreign Keys
    fkEmpresa = db.Column(db.String(36), db.ForeignKey('empresa.oid'), nullable=False)
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False)
    fkProveedorEmpleado = db.Column(db.String(36), db.ForeignKey('proveedor_empleado.oid'), nullable=True)
    fkProveedorEmpresa = db.Column(db.String(36), db.ForeignKey('proveedor_empresa.oid'), nullable=True)
    
    # Relaciones
    empresa = db.relationship('Empresa', foreign_keys=[fkEmpresa])
    sucursal = db.relationship('Sucursal', foreign_keys=[fkSucursal])
    proveedor_empleado = db.relationship('ProveedorEmpleado', foreign_keys=[fkProveedorEmpleado])
    proveedor_empresa = db.relationship('ProveedorEmpresa', foreign_keys=[fkProveedorEmpresa])
    detalles = db.relationship('EntradaMercanciaDetalle', back_populates='entrada_mercancia')
    
    def __repr__(self):
        return f'<EntradaMercancia {self.oid}>'
