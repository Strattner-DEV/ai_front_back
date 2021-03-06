from pickle import FALSE
import jwt 
import json
from copyreg import add_extension
from passlib.hash import bcrypt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

JWT_SECRET = 'myjwtsecret'

app = FastAPI()

class Task(BaseModel):
    id: str
    content: str
    priority: int

class Tasks(BaseModel):
    __root__: dict[str, Task]

class Column(BaseModel):
    id: str
    title: str
    taskIds: list

class Columns(BaseModel):
    __root__: dict[str, Column]

class Board(BaseModel):
    tasks: Tasks
    columns: Columns
    columnOrder: list

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password = fields.CharField(200)
    board = fields.JSONField(default={
    "tasks": {},
    "columns": {
      "column-1": {
        "id": "column-1",
        "title": "To do",
        "taskIds": []
      },
      "column-2": {
        "id": "column-2",
        "title": "Done",
        "taskIds": []
      },
      "column-3": {
        "id": "column-3",
        "title": "In progress",
        "taskIds": []
      }
    },
    "columnOrder": [
      "column-1",
      "column-2",
      "column-3"
    ]
  })

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True, exclude=('board',))

async def authenticate_user(username: str, password: str):
    user = await User.get(username=username)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password"
        )

    return await User_Pydantic.from_tortoise_orm(user)

@app.get('/board')
async def get_board(user: User_Pydantic = Depends(get_current_user)):
    user = await User.get(id=user.id)
    print(user.board)
    return {'board': user.board}


@app.post('/board')
async def save_board(board: Board, user: User_Pydantic = Depends(get_current_user)):
    user = await User.get(id=user.id)
    user.board = board.json()
    await user.save()

    return {"status": "success"}

number = 1

@app.post('/add_task') #TODO: Encontrar forma de pegar o valor da coluna certa
async def add_task(id_number: int, content: str, priority: int, user: User_Pydantic = Depends(get_current_user)):
    user = await User.get(id=user.id)
    print(user.board)
    user.board["tasks"].update({f'task-{id_number}' : {'id' : f'task-{id_number}', 'content' : f'{content}','priority' : priority}})
    user.board["columns"]["column-1"]["taskIds"].append(f'task-{id_number}')
    await user.save()

    return {"status": "success"}

@app.post('/users')
async def create_user(user_in: UserIn_Pydantic):
    user = User(username=user_in.username, password=bcrypt.hash(user_in.password))
    await user.save()
    user_obj = await User_Pydantic.from_tortoise_orm(user)

    token = jwt.encode(user_obj.dict(), JWT_SECRET)
    return {"access_token": token}

@app.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password"
        )
    
    user_obj = await User_Pydantic.from_tortoise_orm(user)
    token = jwt.encode(user_obj.dict(), JWT_SECRET)
    return {"access_token": token}

register_tortoise(
    app,
    db_url='postgres://postgres:Password1@127.0.0.1:5432/postgres',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)

# {
#         'tasks' : {
#             'task-1' : {'id' : 'task-1', 'content' : 'create'},
#             'task-2' : {'id' : 'task-2', 'content' : 'delete'},
#             'task-3' : {'id' : 'task-3', 'content' : 'idk'},
#             'task-4' : {'id' : 'task-4', 'content' : 'Coelho'},
#         },
#         'columns' : {
#             'column-1' : {
#                 'id' : 'column-1',
#                 'title' : 'To do',
#                 'taskIds' : ['task-3', 'task-4']
#             },
#             'column-2' : {
#                 'id' : 'column-2',
#                 'title' : 'In progress',
#                 'taskIds' : ['task-2']
#             },
#             'column-3' : {
#                 'id' : 'column-3',
#                 'title' : 'Done',
#                 'taskIds' : ['task-1']
#             }
#         },
#         'columnOrder' : ['column-1', 'column-2', 'column-3']
#     }


