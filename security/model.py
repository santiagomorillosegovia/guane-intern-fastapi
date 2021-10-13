from pydantic import BaseModel, Field, EmailStr



class UserSchema(BaseModel):
    name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Santiago",
                "last_name": "Morillo",
                "email": "santiagomorillosegovia@gmail.com",
                "password": "weakpassword"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "santiagomorillosegovia@gmail.com",
                "password": "weakpassword"
            }
        }

