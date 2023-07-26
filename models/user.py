"""
Modelo usarios
"""
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

# creacion de la tabla users
users = Table("users", meta, 
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255))
)

# unimos la conexion con la tabla
meta.create_all(engine)