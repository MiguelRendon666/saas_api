from app import db
from app.models.base import BaseObject

class EntradaMercancia(BaseObject):
    __tablename__ = 'entrada_mercancia'
    
    fecha = db.Column(db.DateTime, nullable=False, index=True)
    costo_subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    descuento = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    costo_total = db.Column(db.Numeric(10, 2), nullable=False)
    observaciones = db.Column(db.Text, nullable=True)
    
    # Foreign Keys
    fkEmpresa = db.Column(db.String(36), db.ForeignKey('empresa.oid'), nullable=False, index=True)
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False, index=True)
    fkProveedorEmpleado = db.Column(db.String(36), db.ForeignKey('proveedor_empleado.oid'), nullable=True, index=True)
    fkProveedorEmpresa = db.Column(db.String(36), db.ForeignKey('proveedor_empresa.oid'), nullable=True, index=True)
    
    # Relaciones
    empresa = db.relationship('Empresa', foreign_keys=[fkEmpresa])
    sucursal = db.relationship('Sucursal', foreign_keys=[fkSucursal])
    proveedor_empleado = db.relationship('ProveedorEmpleado', foreign_keys=[fkProveedorEmpleado])
    proveedor_empresa = db.relationship('ProveedorEmpresa', foreign_keys=[fkProveedorEmpresa])
    detalles = db.relationship('EntradaMercanciaDetalle', back_populates='entrada_mercancia')
    
    # Índices
    __table_args__ = (
        db.Index('ix_entrada_mercancia_sucursal_fecha', 'fkSucursal', 'fecha'),
        db.Index('ix_entrada_mercancia_proveedor_fecha', 'fkProveedorEmpleado', 'fecha'),
    )
    
    def __repr__(self):
        return f'<EntradaMercancia {self.oid}>'
