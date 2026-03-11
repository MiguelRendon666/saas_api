from app import db
from app.models.base import BaseObject

class Usuario(BaseObject):
    __tablename__ = 'usuario'
    
    usuario = db.Column(db.String(100), nullable=False, unique=True, index=True)
    contraseña = db.Column(db.String(255), nullable=False)
    apellidoPaterno = db.Column(db.String(100), nullable=False)
    apellidoMaterno = db.Column(db.String(100), nullable=False)
    nombres = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    
    # Foreign Keys - referencias a otros microservicios
    fkEmpresa = db.Column(db.String(36), nullable=False, index=True)
    fkSucursal = db.Column(db.String(36), nullable=False, index=True)
    fkSistema = db.Column(db.String(36), nullable=False, index=True)
    
    # Relaciones
    usuario_roles = db.relationship('UsuarioRol', back_populates='usuario')
    
    def __repr__(self):
        return f'<Usuario {self.usuario}>'
