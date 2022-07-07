from fastapi import FastAPI

app = FastAPI()

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


