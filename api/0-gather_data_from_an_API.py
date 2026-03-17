#!/usr/bin/python3
"""Script to get TODO progress for an employee from API."""

import requests
import sys


def main():
    """Main function to fetch and display employee TODO progress."""
    if len(sys.argv) != 2:
        return

    user_id = int(sys.argv[1])

    # URLs
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Fetch data
    todos = requests.get(todos_url).json()
    user = requests.get(user_url).json()

    # Filter tasks for this user
    user_todos = [t for t in todos if t["userId"] == user_id]
    completed_tasks = [t["title"] for t in user_todos if t["completed"]]
    total_tasks = len(user_todos)

    # Print first line exactly as expected
    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    # Print completed tasks with exact formatting (1 tab + 1 space)
    for title in completed_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
