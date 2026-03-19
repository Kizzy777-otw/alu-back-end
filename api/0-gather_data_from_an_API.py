#!/usr/bin/python3
"""Script to get TODO progress for an employee from API."""

import requests
import sys


def main():
    """Main function."""
    if len(sys.argv) != 2:
        return

    user_id = int(sys.argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    response = requests.get(todo_url)

    total_questions = 0
    completed = []
    for todo in response.json():
        if todo['userId'] == user_id:
            total_questions += 1

            if todo['completed']:
                completed.append(todo['title'])

    user_name = requests.get(user_url).json()['name']

    with open('student_output', 'w') as f:
        printer = ("Employee {} is done with tasks({}/{}):".format(user_name,
                   len(completed), total_questions))
        f.write(printer + '\n')

        for q in completed:
            f.write("\t {}\n".format(q))


if __name__ == "__main__":
    main()
