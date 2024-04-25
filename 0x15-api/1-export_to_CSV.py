#!/usr/bin/python3
""" Export api response to comma seperated value file (csv)"""
import csv
import requests
import sys


def main():
    """
    main function which is the first poioint of execution for running this
    script to get the userName, ID, title
    """
    # - Variables to be used
    complete = 0
    total = 0
    username = ''
    args = int(sys.argv[1])
    userUrl = requests.get("https://jsonplaceholder.typicode.com/users")
    todoUrl = requests.get("https://jsonplaceholder.typicode.com/todos")

    userUrl.json()
    for user in userUrl.json():
        if user["id"] == args:
            name = user.get("name")
            username = user.get("username")

    for todo in todoUrl.json():
        if todo.get("userId") == args:
            if todo.get("completed") is True:
                complete += 1

    for todo in todoUrl.json():
        if todo.get("userId") == args:
            if todo["completed"] is True or todo["completed"] is False:
                total += 1

    new_list = []
    default = []

    for todo in todoUrl.json():
        if todo["userId"] == args:
            new_list = [
                todo["userId"],
                username,
                todo["completed"],
                todo["title"]
            ]
            default.append(new_list)

    filename = f"{args}.csv"
    with open(filename, "w", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(default)


if __name__ == "__main__":
    main()
