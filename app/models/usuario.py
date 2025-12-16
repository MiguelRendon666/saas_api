from app import db
from app.models.base_contacto import BaseContactoObject

class Usuario(BaseContactoObject):
    __tablename__ = 'usuario'
    
    usuario = db.Column(db.String(100), nullable=False, unique=True, index=True)
    contraseña = db.Column(db.String(255), nullable=False)
    apellidoPaterno = db.Column(db.String(100), nullable=False)
    apellidoMaterno = db.Column(db.String(100), nullable=False)
    nombres = db.Column(db.String(200), nullable=False)
    
    # Foreign Keys
    fkEmpresa = db.Column(db.String(36), db.ForeignKey('empresa.oid'), nullable=False, index=True)
    fkSucursal = db.Column(db.String(36), db.ForeignKey('sucursal.oid'), nullable=True, index=True)
    
    # Relaciones
    empresa = db.relationship('Empresa', foreign_keys=[fkEmpresa], back_populates='usuario')
    sucursal = db.relationship('Sucursal', foreign_keys=[fkSucursal], back_populates='usuarios')
    usuario_roles = db.relationship('UsuarioRol', back_populates='usuario')
    
    def __repr__(self):
        return f'<Usuario {self.usuario}>'
