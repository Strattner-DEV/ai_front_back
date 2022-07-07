from fastapi import FastAPI
from pydantic import BaseModel
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

app = FastAPI()

class Task(BaseModel):
    id: str
    content: str

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
    username: fields.CharField(50, unique=True)
    password: fields.CharField(200)
    board = fields.JSONField(default={"tasks": {}, "columns": {},"columnOrder": [] })

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True, exclude=('board',))


@app.get('/board')
def get_board():
    board_data = {
        'tasks' : {
            'task-1' : {'id' : 'task-1', 'content' : 'create'},
            'task-2' : {'id' : 'task-2', 'content' : 'delete'},
            'task-3' : {'id' : 'task-3', 'content' : 'idk'},
            'task-4' : {'id' : 'task-4', 'content' : 'Coelho'},
        },
        'columns' : {
            'column-1' : {
                'id' : 'column-1',
                'title' : 'To do',
                'taskIds' : ['task-3', 'task-4']
            },
            'column-2' : {
                'id' : 'column-2',
                'title' : 'In progress',
                'taskIds' : ['task-2']
            },
            'column-3' : {
                'id' : 'column-3',
                'title' : 'Done',
                'taskIds' : ['task-1']
            }
        },
        'columnOrder' : ['column-1', 'column-2', 'column-3']
    }
    return {'board': board_data }


