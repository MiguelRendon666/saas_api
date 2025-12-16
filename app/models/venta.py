from app import db
from app.models.base import BaseObject
from app.enums import Pago

class Venta(BaseObject):
    __tablename__ = 'venta'
    
    numero_folio = db.Column(db.Integer, nullable=False, index=True)
    folio_completo = db.Column(db.String(100), nullable=False, unique=True, index=True)
    fecha = db.Column(db.DateTime, nullable=False, index=True)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    descuento_general = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    pago = db.Column(db.Enum(Pago), nullable=False, index=True)
    
    # Foreign Keys
    fkEmpresa = db.Column(db.String(36), db.ForeignKey('empresa.oid'), nullable=False, index=True)
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False, index=True)
    fkUsuario = db.Column(db.String(36), db.ForeignKey('usuario.oid'), nullable=False, index=True)
    
    # Relaciones
    empresa = db.relationship('Empresa', foreign_keys=[fkEmpresa])
    sucursal = db.relationship('Sucursal', foreign_keys=[fkSucursal])
    usuario = db.relationship('Usuario', foreign_keys=[fkUsuario])
    detalles = db.relationship('VentaDetalle', back_populates='venta')
    
    # Índices
    __table_args__ = (
        db.Index('ix_venta_sucursal_fecha', 'fkSucursal', 'fecha'),
        db.Index('ix_venta_usuario_fecha', 'fkUsuario', 'fecha'),
        db.Index('ix_venta_sucursal_folio', 'fkSucursal', 'numero_folio', unique=True),
    )
    
    def __repr__(self):
        return f'<Venta {self.folio_completo}>'
