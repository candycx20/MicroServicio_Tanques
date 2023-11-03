# models/schemas/cliente.py

from pydantic import BaseModel

class ClienteCreate(BaseModel):
    dpi: str
    nombre: str
    puntos: float


