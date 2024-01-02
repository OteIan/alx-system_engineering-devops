#!/usr/bin/python3
"""Returns Todo list for a given employee id"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    result = {u['id']: [{"task": i['title'],
                         "completed": i['completed'],
                         "username": u['username']
                         } for i in requests.get(url + "todos",
                                                 params={"userId": u['id']}
                                                 ).json()]
              for u in user}

    with open("todo_all_employees.json", "w") as f:
        json.dump(result, f)
