

from motor.motor_asyncio import AsyncIOMotorClient


#defino una función asíncrona para conectarme a mi BD MONGO
async def get_DB():
    cliente = AsyncIOMotorClient("mongodb://localhost:27017")
    db = cliente["peliculas"]

    return db