#!/usr/bin/python3
"""Export the TODO list data of all employees to a JSON file."""
import json
import urllib.request
from collections import OrderedDict


def fetch(url):
    """Return the parsed JSON found at url."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = fetch("{}/users".format(base_url))
    todos = fetch("{}/todos".format(base_url))

    data = OrderedDict()
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                item = OrderedDict()
                item["username"] = username
                item["task"] = task.get("title")
                item["completed"] = task.get("completed")
                tasks.append(item)
        data[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
