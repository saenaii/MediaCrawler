import json

import requests

import config


def listPendingTask() -> dict:
    resp = requests.get("http://localhost/api/task")
    data = resp.json()

    tasks = {}
    for item in data["data"]:
        tasks[item["NoteID"]] = item["TaskID"]
    return tasks

def toList(taskMap:dict):
    tasks = []
    for k in taskMap:
        tasks.append(k)
    return tasks

def updateTask(taskID:str, status:bool, body:dict):
    postBody = {'taskID': taskID, 'status': status, 'data': body}
    requests.post("http://localhost/api/xhs/detail", data = json.dumps(postBody, separators=(',', ':'), ensure_ascii=False))
