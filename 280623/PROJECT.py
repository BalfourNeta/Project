import json


class ClassInstance:
    def __init__(self, major1, major2, points_math, points_english):
        self.major1 = major1
        self.major2 = major2
        self.points_math = points_math
        self.points_english = points_english

    def to_dict(self):
        return {
            'major1': self.major1,
            'major2': self.major2,
            'points_math': self.points_math,
            'points_english': self.points_english
        }


def create_class_instance():
    major1 = input("Enter your first major: ")
    major2 = input("Enter your second major: ")
    points_math = int(input("Enter your points in math (3-5): "))
    while points_math not in range(3, 6):
        print("Points in math must be between 3 and 5.")
        points_math = int(input("Enter your points in math (3-5): "))
    points_english = int(input("Enter your points in English (3-5): "))
    while points_english not in range(3, 6):
        print("Points in English must be between 3 and 5.")
        points_english = int(input("Enter your points in English (3-5): "))

    return ClassInstance(major1, major2, points_math, points_english)


def save_user_info(users_data):
    with open("users_info.json", "w") as json_file:
        json.dump(users_data, json_file)


def load_user_info():
    try:
        with open("users_info.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}


# Dictionary to store user information
users_info = load_user_info()


def display_completed_tasks(student_info):
    if 'tasks' in student_info:
        print("Completed tasks:")
        for idx, task in enumerate(student_info['tasks'], start=1):
            if task['completed']:
                print(f"Task {idx}:")
                print(f"Subject: {task['subject']}")
                print(f"Details: {task['details']}")
                print(f"Due Date: {task['due_date']}")
                print()  # Print an empty line for better readability
    else:
        print("No tasks assigned to you.")


def display_incomplete_tasks(student_info):
    if 'tasks' in student_info:
        print("Incomplete tasks:")
        for idx, task in enumerate(student_info['tasks'], start=1):
            if not task['completed']:
                print(f"Task {idx}:")
                print(f"Subject: {task['subject']}")
                print(f"Details: {task['details']}")
                print(f"Due Date: {task['due_date']}")
                print()  # Print an empty line for better readability
    else:
        print("No tasks assigned to you.")


def display_tasks(student_info):
    display_incomplete_tasks(student_info)
    display_completed_option = input("Do you want to view completed tasks? (yes/no): ")
    if display_completed_option.lower() == "yes":
        display_completed_tasks(student_info)


def mark_task_completed(student_info):
    if 'tasks' in student_info:
        task_idx = int(input("Enter the index of the task you want to mark as completed: ")) - 1
        if 0 <= task_idx < len(student_info['tasks']):
            student_info['tasks'][task_idx]['completed'] = True
            save_user_info(users_info)
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
    else:
        print("No tasks assigned to you.")


def add_task_for_student(student_info):
    task_subject = input("Enter the subject of the task: ")
    task_details = input("Enter the details of the task: ")
    task_due_date = input("Enter the due date for the task: ")

    if 'tasks' not in student_info:
        student_info['tasks'] = []

    student_info['tasks'].append({
        'subject': task_subject,
        'details': task_details,
        'due_date': task_due_date,
        'completed': False
    })

    save_user_info(users_info)
    print("Task added successfully.")


def load_tasks():
    try:
        with open("tasks.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}


# Dictionary to store tasks assigned by teachers
tasks = load_tasks()


def main():
    job = int(input("If you are a teacher, enter 0. If you are a student, enter 1: "))

    if job == 0:
        teacher_name = input("Enter your name: ")
        teacher_email = input("Enter your email address: ")

        # Check if teacher information exists
        if teacher_name not in users_info:
            users_info[teacher_name] = {}

        if teacher_email not in users_info[teacher_name]:
            users_info[teacher_name][teacher_email] = {'type': 'teacher'}
            print("Welcome, Teacher!")

        give_task = input("Do you want to give a task for one of your classes? (yes/no): ")
        if give_task.lower() == "yes":
            grade_number = int(input("Enter the grade to give a task to (10/11/12): "))
            class_number = int(input("Enter the class number to give a task to: "))

            task_subject = input("Enter the subject of the task: ")
            task_details = input("Enter the details of the task: ")
            task_due_date = input("Enter the due date for the task: ")

            task_key = f"ca{class_number}_grade_{grade_number}"
            if task_key not in tasks:
                tasks[task_key] = []

            tasks[task_key].append({
                'subject': task_subject,
                'details': task_details,
                'due_date': task_due_date
            })

            with open("tasks.json", "w") as json_file:
                json.dump(tasks, json_file)

    elif job == 1:
        student_name = input("Enter your name: ")
        student_email = input("Enter your email address: ")

        # Check if student information exists
        if student_name not in users_info:
            users_info[student_name] = {}

        if student_email not in users_info[student_name]:
            users_info[student_name][student_email] = {'type': 'student'}

        student_info = users_info[student_name][student_email]

        if student_info['type'] == 'student':
            print("Welcome, Student!")
            display_tasks(student_info)

            if 'tasks' in student_info:
                mark_completed_option = input("Do you want to mark a task as completed? (yes/no): ")
                if mark_completed_option.lower() == "yes":
                    mark_task_completed(student_info)

            add_task_option = input("Do you want to add a task for yourself? (yes/no): ")
            if add_task_option.lower() == "yes":
                add_task_for_student(student_info)
        else:
            print("Invalid student information.")


if __name__ == "__main__":
    main()
