from fastapi import APIRouter, Body, Depends, File, UploadFile
from fastapi.params import File
from config.db import db
from schemas.dog import dogEntity, dogsEntity, userEntity, usersEntity
from security.model import UserLoginSchema, UserSchema
from security.auth.auth_handler import signJWT
from security.auth.auth__bearer import JWTBearer
from models.dog import Dog
from datetime import datetime
from bson import ObjectId
import requests
import json

dog = APIRouter()


@dog.get('/api/dogs', tags=["dogs"])
def show_dogs():

    return dogsEntity(db.dogs.find())


@dog.get('/api/dogs/is_adopted', tags=["dogs"])
def show_adopted():
    return dogsEntity(db.dogs.find({"is_adopted": True}))


@dog.get('/api/dogs/{name}', tags=["dogs"])
def show_dog(name: str):
    return dogsEntity(db.dogs.find({"name": name}))


@dog.post('/api/dogs/{name}', dependencies=[Depends(JWTBearer())], tags=["dogs"])
def create_dog(dog: Dog):
    new_dog = dict(dog)
    del new_dog["create_date"]
    del new_dog["picture"]

    image = requests.get('https://dog.ceo/api/breeds/image/random')
    image = image.json()
    new_dog["picture"] = image["message"]

    new_dog["create_date"] = datetime.now()
    db.dogs.insert_one(new_dog)
    return "Dog Saved"


@dog.put('/api/dogs/{name}', tags=["dogs"])
def edit_dog(name: str, dog: Dog):
    new_dog = dict(dog)
    del new_dog["create_date"]
    del new_dog["picture"]
    db.dogs.find_one_and_update({"name": name}, {"$set": new_dog})
    return "Dog Updated"


@dog.delete('/api/dogs/{name}', tags=["dogs"])
def delete_dog(name: str):
    db.dogs.find_one_and_delete({"name": name})
    return "Dog Deleted"


######################################


@dog.post("/api/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    new_user = dict(user)
    db.users.insert_one(new_user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    users = usersEntity(db.users.find())
    for user in users:
        if user['email'] == data.email and user['password'] == data.password:
            return True
    return False


@dog.post("/api/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }


@dog.get('/api/user', tags=["user"])
def show_users():

    return usersEntity(db.users.find())


@dog.get('/api/user/{id}', tags=["user"])
def show_user(id: str):
    return usersEntity(db.users.find({"_id": ObjectId(id)}))


@dog.put('/api/user/{id}', tags=["user"])
def edit_user(id: str, user: UserSchema):
    new_user = dict(user)
    db.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": new_user})
    return "User Updated"


@dog.delete('/api/user/{id}', tags=["user"])
def delete_user(id: str):
    db.users.find_one_and_delete({"_id": ObjectId(id)})
    return "User Deleted"


#######################

@dog.post('/api/file', tags=["file"])
async def upload_file(file: UploadFile = File(...)):

    file_content = await file.read()

    files = [
        ('file', (file.filename, file_content, file.content_type))
    ]

    file_response = requests.post(
        'https://gttb.guane.dev/api/files', files=files)

    return file_response.json()
