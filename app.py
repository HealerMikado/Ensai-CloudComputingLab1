from typing import Union
from fastapi import FastAPI
import requests
import uvicorn

from task import Task
from task_dao import TaskDAO 
app = FastAPI()

# Pour faire fonctionner ce code vous devez être sur le réseau de l'ensai
# (ou avoir un base de données postgres chez vous), initialiser la base
# avec le contenu du fichier init_db.sql, et modifier le fichier .env
# pour que le code se connecte à la base

@app.get("/task/")
async def get_task_by_user(user :Union[str, None]=None):
    if user:
        tasks = TaskDAO().find_all_task_by_user(user)
    else :
        tasks = TaskDAO().find_all_task()
    return {
        "Count": len(tasks),
        "Tasks" : tasks}


@app.get("/task/{id}")
async def get_task(id :int):
    return TaskDAO().find_all_task_by_id(id)

@app.get("/instance")
async def get_instance_id(id :int):
    return {"instanceId":requests.get("http://169.254.169.254/latest/meta-data/instance-id").text}


@app.post("/task/")
async def post_task(task :Task):
    return TaskDAO().create_task(task)

@app.put("/task/{id}")
async def update_task(id:int, task :Task):
    if TaskDAO().find_all_task_by_id(id) :
        return TaskDAO().update_task(task, id)
    else :
        return TaskDAO().create_task(task, id)

@app.delete("/task/{id}")
async def delete_task(id:int):
    return TaskDAO().delete_task(id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)