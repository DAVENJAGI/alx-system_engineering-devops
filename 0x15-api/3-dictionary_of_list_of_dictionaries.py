#!/usr/bin/python3
"""
converts data to json format
"""

import csv
import json
import requests
import sys


def all_to_json():
    """Function that converts data to csv format"""
    data = {}
    for id in range(1, 11):
        req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(id))
        user = req.json()
        req = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        )
        todos = req.json()
        taskList = []
        for todo in todos:
            task = {
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"],
            }
            taskList.append(task)
        data[str(user["id"])] = taskList

    f_name = "todo_all_employees.json"
    with open(f_name, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    all_to_json()
