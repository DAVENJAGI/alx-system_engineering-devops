#!/usr/bin/python3
"""
converts dta to csv format
"""

import csv
import json
import requests
import sys


def change_to_csv(employee_ID):
    """Function that converts data to csv format"""
    # a get request to get the users data
    url = f"https://jsonplaceholder.typicode.com/users/{employee_ID}"
    user_response = requests.get(url)

    url_1 = f'https://jsonplaceholder.typicode.com/users/{employee_ID}/todos'
    user_response_1 = requests.get(url_1)
    to_data = user_response_1.json()

    f_name = "{}.csv".format(employee_ID)
    with open(f_name, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in to_data:
            writer.writerow([user["id"], user["username"],
                             to_data["completed"], to_data["title"]])


if __name__ == "__main__":
    change_to_csv(int(sys.argv[1]))
