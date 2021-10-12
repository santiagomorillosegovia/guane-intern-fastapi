from fastapi import APIRouter
from config.db import db
from schemas.dog import dogEntity, dogsEntity
from models.dog import Dog
from datetime import datetime
import requests
import json


dog = APIRouter()


@dog.get('/api/dogs', tags=["dogs"])
def show_dogs():
   
   return dogsEntity(db.dogs.find())
   



@dog.get('/api/dogs/is_adopted', tags=["dogs"])
def show_adopted():
   return dogsEntity(db.dogs.find( { "is_adopted": True }))


@dog.get('/api/dogs/{name}', tags=["dogs"])
def show_dog(name: str):
    return dogsEntity(db.dogs.find( { "name": name } ))



@dog.post('/api/dogs/{name}', tags=["dogs"])
def create_dog(dog: Dog):
    new_dog = dict(dog)
    del new_dog ["create_date"]
    del new_dog ["id"]
    del new_dog["picture"]


    image = requests.get('https://dog.ceo/api/breeds/image/random')
    image=image.json()
    new_dog ["picture"]= image["message"]
   
    new_dog ["create_date"]= datetime.now()
    db.dogs.insert_one(new_dog)
    print(new_dog)
    return "Dog Saved"



@dog.put('/api/dogs/{name}', tags=["dogs"])
def edit_dog(name: str, dog: Dog):
    new_dog = dict(dog)
    del new_dog ["create_date"]
    del new_dog ["id"]
    db.dogs.find_one_and_update({ "name": name },{"$set": new_dog})
    return "Dog Updated"



@dog.delete('/api/dogs/{name}', tags=["dogs"])
def delete_dog(name: str):
    db.dogs.find_one_and_delete({ "name": name })
    return "Dog Deleted"







