from app import db
from app.models.base import BaseObject

class CorteCaja(BaseObject):
    __tablename__ = 'corte_caja'
    
    fecha = db.Column(db.DateTime, nullable=False, index=True)
    monto_inicial = db.Column(db.Numeric(10, 2), nullable=False)
    monto_final = db.Column(db.Numeric(10, 2), nullable=False)
    esperado = db.Column(db.Numeric(10, 2), nullable=False)
    diferencia = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Foreign Keys
    fkUsuario = db.Column(db.String(36), db.ForeignKey('usuario.oid'), nullable=False, index=True)
    fkTurno = db.Column(db.String(36), db.ForeignKey('turno_sucursal.oid'), nullable=False, index=True)
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False, index=True)
    
    # Relaciones
    usuario = db.relationship('Usuario', foreign_keys=[fkUsuario])
    turno = db.relationship('TurnoSucursal', foreign_keys=[fkTurno], back_populates='cortes_caja')
    sucursal = db.relationship('Sucursal', foreign_keys=[fkSucursal])
    
    # Índices
    __table_args__ = (
        db.Index('ix_corte_caja_sucursal_fecha', 'fkSucursal', 'fecha'),
        db.Index('ix_corte_caja_usuario_fecha', 'fkUsuario', 'fecha'),
        db.Index('ix_corte_caja_turno_fecha', 'fkTurno', 'fecha'),
    )
    
    def __repr__(self):
        return f'<CorteCaja {self.oid}>'
