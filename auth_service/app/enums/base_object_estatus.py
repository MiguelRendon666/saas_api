from enum import Enum

class BaseObjectEstatus(str, Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    ELIMINADO = "Eliminado"
