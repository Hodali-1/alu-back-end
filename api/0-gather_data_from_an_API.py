#!/usr/bin/python3
"""Return information about an employee's TODO list progress using a REST API."""
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

    done = [task.get("title") for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
