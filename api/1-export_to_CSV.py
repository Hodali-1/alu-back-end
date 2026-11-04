#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file using a REST API."""
import csv
import json
import sys
import urllib.request


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

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
