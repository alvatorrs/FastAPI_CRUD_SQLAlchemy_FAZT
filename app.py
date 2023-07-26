from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title='REST API con MySQL',
    description= 'API utilizando SQLAlchemy con MySQL',
    version= '0.0.1',
    openapi_tags= [
        {
            'name': 'users',
            'description': 'users routes'
        },
        {
            'name': 'home',
            'description': 'main page API'
        }
    ]
)

app.include_router(user) # incluimos las rutas que vengan de user

@app.get('/', tags=['home'])
def home():
    return 'Hello world'
