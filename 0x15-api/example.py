#!/usr/bin/python3

import json
import requests
import sys

employee_ID = sys.argv[1]

#a get request to get the users data
url =  f"https://jsonplaceholder.typicode.com/users/{employee_ID}"
user_response = requests.get(url)

#parsing the user data to json format
user_data = user_response.json()

#a get request to get the users to do dataand parsing it to json
url_1 = f'https://jsonplaceholder.typicode.com/todos/{employee_ID}'

to_do = requests.get(url_1)
to_do_data = to_do.json()

with open("file.json", "w") as file:
    json.dump(to_do_data, file)
print("to_do_data loaded to file")


