from pydantic import BaseModel
from typing import Optional

#defino un modelo que coincida con los datos de la pelicula

class Pelicula (BaseModel):
    titulo: str
    estado: str

    class Config:
        orm_mode = True