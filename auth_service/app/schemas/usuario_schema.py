from .base_schema import BaseSchema

class UsuarioSchema(BaseSchema):
    """Schema para serialización y validación de Usuario"""
    
    @staticmethod
    def serialize(usuario):
        """Serializa un usuario a diccionario"""
        data = BaseSchema.serialize_base(usuario)
        data.update({
            'usuario': usuario.usuario,
            'apellidoPaterno': usuario.apellidoPaterno,
            'apellidoMaterno': usuario.apellidoMaterno,
            'nombres': usuario.nombres,
            'telefono': usuario.telefono,
            'email': usuario.email,
            'fkEmpresa': usuario.fkEmpresa,
            'fkSucursal': usuario.fkSucursal,
            'fkSistema': usuario.fkSistema
        })
        # No incluir contraseña en la serialización
        return data
    
    @staticmethod
    def serialize_list(usuarios):
        """Serializa una lista de usuarios"""
        return [UsuarioSchema.serialize(usuario) for usuario in usuarios]
    
    @staticmethod
    def validate_create(data):
        """Valida datos para crear un usuario"""
        errors = []
        
        if not data.get('usuario'):
            errors.append('usuario es requerido')
        if not data.get('contraseña'):
            errors.append('contraseña es requerida')
        if not data.get('apellidoPaterno'):
            errors.append('apellidoPaterno es requerido')
        if not data.get('apellidoMaterno'):
            errors.append('apellidoMaterno es requerido')
        if not data.get('nombres'):
            errors.append('nombres es requerido')
        if not data.get('fkEmpresa'):
            errors.append('fkEmpresa es requerido')
        if not data.get('fkSucursal'):
            errors.append('fkSucursal es requerido')
        if not data.get('fkSistema'):
            errors.append('fkSistema es requerido')
        
        return errors
    
    @staticmethod
    def validate_update(data):
        """Valida datos para actualizar un usuario"""
        # Para update, los campos no son obligatorios
        return []
