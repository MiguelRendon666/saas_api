# SaaS API - Flask Project

Proyecto Flask con SQLAlchemy para gestión de base de datos "saascryption".

## Estructura del Proyecto

```
saas_api/
├── app/
│   ├── __init__.py
│   └── models/
│       ├── __init__.py
│       ├── base.py              # BaseObject, BaseContactoObject, Enumeradores
│       ├── empresa.py
│       ├── usuario.py
│       ├── rol.py
│       ├── permiso.py
│       ├── sucursal.py
│       ├── proveedor.py
│       └── producto.py
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## Modelos

### BaseObject
Clase base para todos los modelos con:
- `oid` (UUID)
- `createdAt` (DateTime)
- `updatedAt` (DateTime)
- `estatus` (Enum: Activo, Inactivo, Eliminado)

### BaseContactoObject
Extiende BaseObject agregando:
- `telefono` (nullable)
- `email` (nullable)

### Modelos Principales
- **Empresa**: Información de empresas con logo, dirección y contacto
- **Usuario**: Usuarios del sistema con credenciales
- **Rol**: Roles del sistema
- **Permiso**: Permisos con flags de crear, editar, desactivar
- **Sucursal**: Sucursales de empresas
- **ProveedorMarca**: Marcas de proveedores
- **ProveedorEmpleado**: Empleados de proveedores
- **Producto**: Productos con unidad de medida

## Instalación

1. Crear entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
- Copiar `.env.example` a `.env`
- Configurar la cadena de conexión a PostgreSQL

4. Crear la base de datos:
```sql
CREATE DATABASE saascryption;
```

5. Ejecutar la aplicación:
```bash
python run.py
```

## Configuración de Base de Datos

El proyecto está configurado para usar PostgreSQL. Ajusta la variable `DATABASE_URL` en el archivo `.env`:

```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/saascryption
```

## Notas Técnicas

- **Tablas**: Nombres en `snake_case`
- **Variables Python**: Nombres en `camelCase`
- **Nullable**: Solo campos en BaseContactoObject son nullable
- **UUIDs**: Todas las tablas usan UUID como primary key
- **Relaciones**: Todas las foreign keys incluyen tanto la columna OID como la referencia al objeto
