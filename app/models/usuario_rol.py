from app import db
from app.models.base import BaseObject

class UsuarioRol(BaseObject):
    __tablename__ = 'usuario_rol'
    
    # Foreign Keys
    fkUsuario = db.Column(db.String(36), db.ForeignKey('usuario.oid'), nullable=False)
    fkRol = db.Column(db.String(36), db.ForeignKey('rol.oid'), nullable=False)
    
    # Relaciones
    usuario = db.relationship('Usuario', back_populates='usuario_roles')
    rol = db.relationship('Rol', back_populates='usuario_roles')
    
    def __repr__(self):
        return f'<UsuarioRol Usuario:{self.fkUsuario} - Rol:{self.fkRol}>'
