"""
Endpoints del usuario
"""
from fastapi import APIRouter, Response, status # definir rutas por separado
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key() # sirve para hacer unico cada uno de los cifrados
f = Fernet(key) # con este objeto ciframos lo que querramos

user = APIRouter()

@user.get('/users', response_model=list[User], tags=['users'])
def get_users():
    users_list = conn.execute(users.select()).fetchall()
    return users_list


@user.post('/users', response_model=User, tags=['users'])
def create_user(user: User):
    new_user = {'name': user.name, 'email': user.email}
    # ciframos la password
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    response = conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
    return response


@user.get('/users/{id}', response_model=User, tags=['users'])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.put('/users/{id}', response_model=User, tags=['users'])
def update_user(id: str, user: User):
    encripted_password = f.encrypt(user.password.encode("utf-8"))
    conn.execute(users.update().values(
        name=user.name, 
        email=user.email, 
        password=encripted_password
    ).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['users'])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)