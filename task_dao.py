from task import Task
from singleton import Singleton
from db_connection import DBConnection


class TaskDAO(metaclass=Singleton):
    def find_all_task(self):
        request = "SELECT id, description, \"user\" FROM task ORDER BY id"
        cursor = DBConnection().cursor
        cursor.execute(request)
        res = cursor.fetchall()
        tasks=[]
        if res :
            for row in res :
                task = Task(
                    id = row["id"]
                    , description = row["description"]
                    , user = row["user"]
                )
                tasks.append(task)
        return tasks

    def find_all_task_by_user(self, user):
        request = "SELECT id, description, \"user\" FROM task WHERE \"user\"=:user"
        cursor = DBConnection().cursor()
        cursor.execute(request, {"user":user})
        res = cursor.fetchall()
        tasks=[]
        if res :
            for row in res :
                task = Task(
                    id = row["id"]
                    , description = row["description"]
                    , user = row["user"]
                )
                tasks.append(task)
        return tasks

    def find_all_task_by_id(self, id):
        request = "SELECT id, description, \"user\" FROM task WHERE id=:id"
        cursor = DBConnection().cursor()
        cursor.execute(request, {"id":id})
        res = cursor.fetchone()
        if res :
            task = Task(
                id = res["id"]
                , description = res["description"]
                , user = res["user"]
            )
            return task
        else : return None
    
    def create_task(self, task:Task):
        request = "INSERT INTO task ( description, \"user\") VALUES "\
            "(:description, :user) RETURNING id, description, \"user\""
    
        cursor = DBConnection().cursor()
        cursor.execute(request
            , {"description":task.description
                ,"user":task.user})
        res = cursor.fetchall()
        end = True
        if res :
            for row in res :
                task = Task(
                    id = row["id"]
                    , description = row["description"]
                    , user = row["user"]
                )
        return task
        
    def update_task(self, task, id):
        request = "UPDATE task SET description=:description"\
            ",\"user\"=:user WHERE id=:id RETURNING id, description, \"user\""
        cursor = DBConnection().cursor()
        cursor.execute(request
            , {"description":task.description
                ,"user":task.user
                , "id" : id})
        res = cursor.fetchone()
        if res :
            task = Task(
                id = res["id"]
                , description = res["description"]
                , user = res["user"]
            )
        return task

    def delete_task(self, id):
        request = "DELETE FROM task WHERE id=:id"
        cursor = DBConnection().cursor()
        cursor.execute(request
            , {"id":id})