def dogEntity(item) -> dict:

    return{

        "id": str(item["_id"]),
        "name": item["name"],
        "picture": item["picture"],
        "is_adopted": item["is_adopted"],
        "create_date": item["create_date"],
        "id_user": item["id_user"]

    }



def dogsEntity(entity) -> list:

    return [dogEntity(item) for item in entity]



def userEntity(item) -> dict:

    return{

        "id": str(item["_id"]),
        "name": item["name"],
        "last_name": item["last_name"],
        "email": item["email"],
        "password": item["password"]

    }



def usersEntity(entity) -> list:

    return [userEntity(item) for item in entity]