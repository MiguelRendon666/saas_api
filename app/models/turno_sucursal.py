from app import db
from app.models.base import BaseObject

class TurnoSucursal(BaseObject):
    __tablename__ = 'turno_sucursal'
    
    nombre = db.Column(db.String(100), nullable=False, index=True)
    hora_entrada = db.Column(db.Time, nullable=False)
    hora_salida = db.Column(db.Time, nullable=False)
    hora_corte = db.Column(db.Time, nullable=False)
    
    # Foreign Keys
    fkEmpresa = db.Column(db.String(36), db.ForeignKey('empresa.oid'), nullable=False, index=True)
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=False, index=True)
    
    # Relaciones
    empresa = db.relationship('Empresa', foreign_keys=[fkEmpresa])
    sucursal = db.relationship('Sucursal', foreign_keys=[fkSucursal])
    cortes_caja = db.relationship('CorteCaja', back_populates='turno')
    
    # Índices
    __table_args__ = (
        db.Index('ix_turno_sucursal_empresa', 'fkEmpresa', 'fkSucursal'),
    )
    
    def __repr__(self):
        return f'<TurnoSucursal {self.nombre}>'
