from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from app.models.usuario import Usuario
from app.utils import verify_password
from app.enums import BaseObjectEstatus
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# POST /auth/login - Login único
@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Autentica un usuario y retorna tokens JWT.
    
    Body:
        {
            "usuario": "username",
            "contraseña": "password"
        }
    
    Returns:
        {
            "access_token": "...",
            "refresh_token": "...",
            "usuario": {...}
        }
    """
    try:
        data = request.get_json()
        
        # Validar datos
        if not data:
            return jsonify({'errors': ['No se proporcionaron datos']}), 400
        
        usuario_str = data.get('usuario')
        password = data.get('contraseña')
        
        if not usuario_str:
            return jsonify({'errors': ['usuario es requerido']}), 400
        
        if not password:
            return jsonify({'errors': ['contraseña es requerida']}), 400
        
        # Buscar usuario
        usuario = Usuario.query.filter(
            Usuario.usuario == usuario_str,
            Usuario.estatus == BaseObjectEstatus.ACTIVO
        ).first()
        
        if not usuario:
            return jsonify({'errors': ['Credenciales inválidas']}), 401
        
        # Verificar contraseña con Argon2
        if not verify_password(usuario.contraseña, password):
            return jsonify({'errors': ['Credenciales inválidas']}), 401
        
        # Crear tokens JWT
        access_token = create_access_token(
            identity=usuario.oid,
            expires_delta=timedelta(hours=1)
        )
        refresh_token = create_refresh_token(
            identity=usuario.oid,
            expires_delta=timedelta(days=30)
        )
        
        # Retornar tokens y datos del usuario (sin contraseña)
        from app.schemas.usuario_schema import UsuarioSchema
        
        return jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'usuario': UsuarioSchema.serialize(usuario)
        }), 200
        
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 500
