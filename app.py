from fastapi import FastAPI
from routes.dog import dog


app = FastAPI()
app.include_router(dog)
