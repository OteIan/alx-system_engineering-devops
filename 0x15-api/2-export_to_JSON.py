#!/usr/bin/python3
"""Returns Todo list for a given employee id
and dumps into a json file"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = argv[1]

    user = requests.get(url + f"users/{id}").json()
    todos = requests.get(url + f"todos", params={"userId": id}).json()

    r = {id: [{"task": i['title'],
               "completed": i['completed'],
               "username": user['username']} for i in todos]}

    file_name = f"{id}.json"
    with open(file_name, "w") as f:
        json.dump(r, f)
