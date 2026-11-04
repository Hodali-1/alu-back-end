#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file using a REST API."""
import json
import sys
import urllib.request
from collections import OrderedDict


def fetch(url):
    """Return the parsed JSON found at url."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = fetch("{}/users/{}".format(base_url, user_id))
    todos = fetch("{}/todos?userId={}".format(base_url, user_id))
    username = user.get("username")

    tasks = []
    for task in todos:
        item = OrderedDict()
        item["task"] = task.get("title")
        item["completed"] = task.get("completed")
        item["username"] = username
        tasks.append(item)

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({user_id: tasks}, json_file)
