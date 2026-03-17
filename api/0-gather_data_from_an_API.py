#!/usr/bin/python3
"""Script to get TODO progress for an employee from API."""

import requests
import sys


def main():
    """Fetch and display an employee's TODO list progress."""
    if len(sys.argv) != 2:
        return

    user_id = int(sys.argv[1])

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Fetch data
    todos = requests.get(todos_url).json()
    user = requests.get(user_url).json()

    # Safely get user name
    user_name = user.get("name", "Unknown")

    # Filter tasks for this user
    user_todos = [t for t in todos if t.get("userId") == user_id]
    completed_tasks = [t.get("title") for t in user_todos if t.get("completed")]
    total_tasks = len(user_todos)

    # Print first line (split to respect PEP8)
    first_line = (
        f"Employee {user_name} is done with tasks"
        f"({len(completed_tasks)}/{total_tasks}):"
    )
    print(first_line)

    # Print completed tasks with exact formatting
    for title in completed_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
