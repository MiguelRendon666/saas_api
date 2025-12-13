from app import db
from app.models.base import BaseObject

class PermisoAsignado(BaseObject):
    __tablename__ = 'permisos_asignados'
    
    # Foreign Keys
    fkPermiso = db.Column(db.String(36), db.ForeignKey('permisos.oid'), nullable=False)
    fkRol = db.Column(db.String(36), db.ForeignKey('rol.oid'), nullable=False)
    
    # Permisos CRUD
    crear = db.Column(db.Boolean, nullable=False, default=False)
    editar = db.Column(db.Boolean, nullable=False, default=False)
    desactivar = db.Column(db.Boolean, nullable=False, default=False)
    
    # Relaciones
    permiso = db.relationship('Permiso', back_populates='permisos_asignados')
    rol = db.relationship('Rol', back_populates='permisos_asignados')
    
    def __repr__(self):
        return f'<PermisoAsignado Rol:{self.fkRol} - Permiso:{self.fkPermiso}>'
