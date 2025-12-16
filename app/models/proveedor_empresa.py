from app import db
from app.models.base import BaseObject

class ProveedorEmpresa(BaseObject):
    __tablename__ = 'proveedor_empresa'
    
    clave = db.Column(db.String(50), nullable=False, unique=True, index=True)
    
    # Foreign Keys
    fkProveedorEmpleado = db.Column(db.String(36), db.ForeignKey('proveedor_empleado.oid'), nullable=False, index=True)
    fkEmpresa = db.Column(db.String(36), db.ForeignKey('empresa.oid'), nullable=False, index=True)
    
    # Relaciones
    proveedor_empleado = db.relationship('ProveedorEmpleado', back_populates='proveedor_empresas')
    empresa = db.relationship('Empresa', back_populates='proveedor_empresas')
    
    # Índices
    __table_args__ = (
        db.Index('ix_proveedor_empresa_unique', 'fkProveedorEmpleado', 'fkEmpresa', unique=True),
    )
    
    def __repr__(self):
        return f'<ProveedorEmpresa Proveedor:{self.fkProveedorEmpleado} - Empresa:{self.fkEmpresa}>'
