from fastapi import FastAPI, Path, status, Body, HTTPException, Request, Form
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/')
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, "users": users})


@app.get('/user/{user_id}')
def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        user = [i for i in users if i.id == user_id][0]
        return templates.TemplateResponse('users.html', {'request': request, 'user': user})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.post('/user/{username}/{age}')
def add_user(username: Annotated[str, Path(mix_length=5, max_length=20, description='Enter Username',
                                           example='UrbanUser')],
             age: Annotated[int, Path(le=120, ge=18, description='Enter Age', example='24')]) -> User:
    user_id = len(users) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      username: Annotated[str, Path(mix_length=5, max_length=20, description='Enter Username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(le=120, ge=18, description='Enter Age', example='24')]
                      ) -> User:
    try:
        user = [i for i in users if i.id == user_id][0]
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        user = [i for i in users if i.id == user_id][0]
        users.pop(users.index(user))
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
