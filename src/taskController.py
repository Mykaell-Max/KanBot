from mongo.mongoConfig import tasks
from datetime import datetime

def add_task(taskname, description, responsible):
    if tasks.find_one({'name': taskname}) != None:
        raise ValueError(f'There is already a task using this name!')
    else:
        task = {
        "name": taskname,
        "description": description,
        "responsible": responsible,
        "status": "Pending",
        "created_at": datetime.now()
        }
        tasks.insert_one(task)


def update_task(taskname, newstatus):
    if tasks.find_one({'name': taskname}) == None:
        raise ValueError(f'This task does not exist!')
    elif newstatus not in ['Pending', 'In progress', 'Done']:
        raise ValueError(f"Invalid status. The status must be 'Pending', 'In progress', or 'Done'.")
    else:
        tasks.update_one({"name": taskname}, {"$set": {"status": newstatus}})


def delete_task(taskname):
    if tasks.find_one({'name': taskname}) == None:
        raise ValueError(f'This task does not exist!')
    else:
        tasks.delete_one({"name": taskname})


def view_all_tasks():
    return [(task['name'], task['status']) for task in tasks.find()]


def view_one_task(taskname):
    task = tasks.find_one({'name': taskname})
    if task == None:
        raise ValueError(f'This task does not exist!')
    else:
        return task