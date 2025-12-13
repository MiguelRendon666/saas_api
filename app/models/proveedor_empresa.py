from app import db
from app.models.base import BaseObject

class ProveedorEmpresa(BaseObject):
    __tablename__ = 'proveedor_empresa'
    
    # Foreign Keys
    fkProveedorEmpleado = db.Column(db.String(36), db.ForeignKey('proveedor_empleado.oid'), nullable=False)
    fkEmpresa = db.Column(db.String(36), db.ForeignKey('empresa.oid'), nullable=False)
    
    # Relaciones
    proveedor_empleado = db.relationship('ProveedorEmpleado', back_populates='proveedor_empresas')
    empresa = db.relationship('Empresa', back_populates='proveedor_empresas')
    
    def __repr__(self):
        return f'<ProveedorEmpresa Proveedor:{self.fkProveedorEmpleado} - Empresa:{self.fkEmpresa}>'
