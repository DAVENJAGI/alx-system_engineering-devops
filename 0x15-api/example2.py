#!/usr/bin/python3

import csv
import json
import requests
import sys

employee_ID = sys.argv[1]

# a get request to get the users data
url = f"https://jsonplaceholder.typicode.com/users/{employee_ID}"
user_response = requests.get(url).json()

""" a get request to get the user's
to do data from /users/employee_ID and parsing it to json"""
url_1 = f'https://jsonplaceholder.typicode.com/users/{employee_ID}/todos'

user_response = requests.get(url_1).json()

#EMPLOYEE_NAME = user_response('username')


with open("2.csv", "w") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(user_response)


if __name__ == "__main__":
    pass
