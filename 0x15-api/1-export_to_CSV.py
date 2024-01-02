#!/usr/bin/python3

import csv
import json
import requests
import sys

employee_ID = sys.argv[1]

# a get request to get the users data
url = f"https://jsonplaceholder.typicode.com/users/{employee_ID}"
user_response = requests.get(url).json()

url_1 = f'https://jsonplaceholder.typicode.com/users/{employee_ID}/todos'

user_response_1 = requests.get(url_1)
to_do_data = user_response_1.json()

with open("2.csv", "w", Newline="") as file:
    fieldname = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
    writer = csv.DictWriter(file, fieldname=fieldname)
    writer.writeheader()
    
    for task in to_do_data:
        writer.writerow({
            "USER_ID": employee_id,
            "USERNAME": employee_name,
            "TASK_COMPLETED_STATUS": str(task["completed"])
            "TASK_TITLE": task["title"]
            })


if __name__ == "__main__":
    pass
