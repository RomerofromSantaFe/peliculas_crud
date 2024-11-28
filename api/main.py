from fastapi import FastAPI, HTTPException
from db import get_DB
from modelos import Pelicula
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId



app = FastAPI()



#DEFINICION DE ENDPOINTS
##################################################
#CREATE#
@app.post("/peliculas/", response_model=Pelicula)
async def crear_pelicula(pelicula: Pelicula):
    db = await get_DB()         #me conecto a la BD
    insercion = await db.peliculas.insert_one(pelicula.dict())

    pelicula_insertada = await db.peliculas.find_one({"_id": insercion.inserted_id})

    return Pelicula(**pelicula_insertada) 


##################################################
#READ
@app.get("/peliculas/")
async def listar_peliculas():
    db = await get_DB()
    resultados = await db.peliculas.find().to_list(100)

    #conversion a lista de dicc. legibles por FastApi
    for resultado in resultados:
        resultado["_id"] = str(resultado["_id"])
    return resultados


@app.get("/peliculas/{id}", response_model=Pelicula)
async def buscar(id: str):
    db = await get_DB()
    id_peli = ObjectId(id)
    busqueda = await db.peliculas.find_one({"_id":id_peli})

    if not busqueda:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")

    busqueda["_id"] = str(busqueda["_id"])

    return busqueda

##################################################
#UPDATE
@app.put("/peliculas/{id}",response_model=Pelicula)
async def actualizar(id: str, pelicula:Pelicula):
    db = await get_DB()
    id_peli = ObjectId(id)
    aparicion = await db.peliculas.find_one({"_id":id_peli})

    if not aparicion:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")
    
    actualizacion = await db.peliculas.update_one(
        {"_id": id_peli},
        {"$set":pelicula.dict()}   #nuevos valores
    )

    return {**pelicula.dict(), "_id": id}


##################################################
#DELETE
@app.delete("/peliculas/{id}")
async def eliminar(id: str):
    db = await get_DB()
    id_peli = ObjectId(id)
    resultado = await db.peliculas.delete_one({"_id": id_peli })

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")
    
    return {"message":"Pelicula eliminada correctamente!"}
