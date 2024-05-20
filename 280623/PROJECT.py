import json

# Dictionary to store tasks assigned by teachers
tasks = {}

# Dictionary to store user information
users_info = {}


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
    while True:
        major1 = input("Enter your first major: ")
        major2 = input("Enter your second major: ")
        points_math = int(input("Enter your points in math (3-5): "))
        if 3 <= points_math <= 5:
            break
        else:
            print("Points in math must be between 3 and 5.")

    while True:
        points_english = int(input("Enter your points in English (3-5): "))
        if 3 <= points_english <= 5:
            break
        else:
            print("Points in English must be between 3 and 5.")

    return ClassInstance(major1, major2, points_math, points_english)


def create_classes_for_grade(grade, num_classes):
    classes = []
    print(f"\nFor grade {grade}:")
    for i in range(1, num_classes + 1):
        class_instance = create_class_instance()
        classes.append(class_instance)
    return classes


def save_user_info(name, email, user_type, info):
    if name in users_info and email in users_info[name]:
        # Update existing user information
        users_info[name][email][user_type] = info
    else:
        # Add new user information
        if name not in users_info:
            users_info[name] = {}
        users_info[name][email] = {user_type: info}

    # Save updated user information to JSON file
    with open("users_info.json", "w") as json_file:
        json.dump(users_info, json_file)


def load_users_info():
    try:
        with open("users_info.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}


def load_tasks():
    try:
        with open("tasks.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}


def teacher_info():
    teacher_name = input("Enter your name: ")
    teacher_email = input("Enter your email address: ")

    # Check if teacher information exists
    if teacher_name in users_info and teacher_email in users_info[teacher_name] and 'teacher' in users_info[teacher_name][teacher_email]:
        print("Welcome back, Teacher!")
        # Display tasks given by the teacher
        display_teacher_tasks(teacher_name, teacher_email)
    else:
        teacher_subject = input("What subject do you teach? ")

        if teacher_subject.lower() == "math":
            grade10 = input("Do you teach 10th grade? (yes/no): ")
            if grade10.lower() == "yes":
                math_teacher10 = input("How many units do you teach? (comma-separated): ").split(',')
                math_teacher10 = [int(c) for c in math_teacher10]
                for i in math_teacher10:
                    if 3 <= i <= 5:
                        break
                    else:
                        print("Points in math must be between 3 and 5.")
                        math_teacher10 = input("Please enter valid units between 3 and 5: ").split(',')
                        math_teacher10 = [int(c) for c in math_teacher10]
                for i in math_teacher10:
                    math_classes10 = input(
                        f"Enter the numbers of classes you teach for {i} units (comma-separated): ").split(',')
                    math_classes10 = [int(c) for c in math_classes10]

            grade11 = input("Do you teach 11th grade? (yes/no): ")
            if grade11.lower() == "yes":
                math_teacher11 = input("How many units do you teach? (comma-separated): ").split(',')
                math_teacher11 = [int(c) for c in math_teacher11]
                for i in math_teacher11:
                    if 3 <= i <= 5:
                        break
                    else:
                        print("Points in math must be between 3 and 5.")
                        math_teacher11 = input("Please enter valid units between 3 and 5: ").split(',')
                        math_teacher11 = [int(c) for c in math_teacher11]
                for i in math_teacher11:
                    math_classes11 = input(
                        f"Enter the numbers of classes you teach for {i} units (comma-separated): ").split(',')
                    math_classes11 = [int(c) for c in math_classes11]
                    # You might want to store or use math_classes11 for further logic

            grade12 = input("Do you teach 12th grade? (yes/no): ")
            if grade12.lower() == "yes":
                math_teacher12 = input("How many units do you teach? (comma-separated): ").split(',')
                math_teacher12 = [int(c) for c in math_teacher12]
                for i in math_teacher12:
                    if 3 <= i <= 5:
                        break
                    else:
                        print("Points in math must be between 3 and 5.")
                        math_teacher12 = input("Please enter valid units between 3 and 5: ").split(',')
                        math_teacher12 = [int(c) for c in math_teacher12]

                for i in math_teacher12:
                    math_classes12 = input(
                        f"Enter the numbers of classes you teach for {i} units (comma-separated): ").split(',')
                    math_classes12 = [int(c) for c in math_classes12]

        elif teacher_subject.lower() == "english":
            grade10 = input("Do you teach 10th grade? (yes/no): ")
            if grade10.lower() == "yes":
                english_teacher10 = input("How many units do you teach? (comma-separated): ").split(',')
                english_teacher10 = [int(c) for c in english_teacher10]
                for i in english_teacher10:
                    if 3 <= i <= 5:
                        break
                    else:
                        print("Points in English must be between 3 and 5.")
                        english_teacher10 = input("Please enter valid units between 3 and 5: ").split(',')
                        english_teacher10 = [int(c) for c in english_teacher10]
                for i in english_teacher10:
                    english_classes10 = input(
                        f"Enter the numbers of classes you teach for {i} units (comma-separated): ").split(',')
                    english_classes10 = [int(c) for c in english_classes10]

            grade11 = input("Do you teach 11th grade? (yes/no): ")
            if grade11.lower() == "yes":
                english_teacher11 = input("How many units do you teach? (comma-separated): ").split(',')
                english_teacher11 = [int(c) for c in english_teacher11]
                for i in english_teacher11:
                    if 3 <= i <= 5:
                        break
                    else:
                        print("Points in English must be between 3 and 5.")
                        english_teacher11 = input("Please enter valid units between 3 and 5: ").split(',')
                        english_teacher11 = [int(c) for c in english_teacher11]
                for i in english_teacher11:
                    english_classes11 = input(
                        f"Enter the numbers of classes you teach for {i} units (comma-separated): ").split(',')
                    english_classes11 = [int(c) for c in english_classes11]

            grade12 = input("Do you teach 12th grade? (yes/no): ")
            if grade12.lower() == "yes":
                english_teacher12 = input("How many units do you teach? (comma-separated): ").split(',')
                english_teacher12 = [int(c) for c in english_teacher12]
                for i in english_teacher12:
                    if 3 <= i <= 5:
                        break
                    else:
                        print("Points in English must be between 3 and 5.")
                        english_teacher12 = input("Please enter valid units between 3 and 5: ").split(',')
                        english_teacher12 = [int(c) for c in english_teacher12]
                for i in english_teacher12:
                    english_classes12 = input(
                        f"Enter the numbers of classes you teach for {i} units (comma-separated): ").split(',')
                    english_classes12 = [int(c) for c in english_classes12]

        else:
            grade10 = input("Do you teach 10th grade? (yes/no): ")
            if grade10.lower() == "yes":
                num_grade10 = input("Enter the numbers of classes you teach for 10th grade (comma-separated): ").split(',')
                num_grade10 = [int(c) for c in num_grade10]

            grade11 = input("Do you teach 11th grade? (yes/no): ")
            if grade11.lower() == "yes":
                num_grade11 = input("Enter the numbers of classes you teach for 11th grade (comma-separated): ").split(',')
                num_grade11 = [int(c) for c in num_grade11]

            grade12 = input("Do you teach 12th grade? (yes/no): ")
            if grade12.lower() == "yes":
                num_grade12 =input("Enter the numbers of classes you teach for 10th grade (comma-separated): ").split(',')
                num_grade12 = [int(c) for c in num_grade12]


        # Save teacher information
        save_user_info(teacher_name, teacher_email, 'teacher', {
            'teacher_subject': teacher_subject,
            'math_teacher10': math_teacher10 if 'math_teacher10' in locals() else None,
            'math_teacher11': math_teacher11 if 'math_teacher11' in locals() else None,
            'math_teacher12': math_teacher12 if 'math_teacher12' in locals() else None,
            'math_classes10': math_classes10 if 'math_classes10' in locals() else None,
            'math_classes11': math_classes11 if 'math_classes11' in locals() else None,
            'math_classes12': math_classes12 if 'math_classes12' in locals() else None,
            'english_teacher10': english_teacher10 if 'english_teacher10' in locals() else None,
            'english_teacher11': english_teacher11 if 'english_teacher11' in locals() else None,
            'english_teacher12': english_teacher12 if 'english_teacher12' in locals() else None,
            'english_classes10': english_classes10 if 'english_classes10' in locals() else None,
            'english_classes11': english_classes11 if 'english_classes11' in locals() else None,
            'english_classes12': english_classes12 if 'english_classes12' in locals() else None,
            'num_grade10': num_grade10 if 'num_grade10' in locals() else None,
            'num_grade11': num_grade11 if 'num_grade11' in locals() else None,
            'num_grade12': num_grade12 if 'num_grade12' in locals() else None
        })

def add_task_for_teacher():
    give_task = input("Do you want to give a task for one of your classes? (yes/no): ")
    if give_task.lower() == "yes":
        grade_number = int(input("Enter the grade to give a task to (10/11/12): "))
        if teacher_subject.lower() == "Math" and teacher_subject.lower() == "English":
            unit_number=int(input("Enter the unit number to give a task to: "))
        class_number = input("Enter the classes number to give a task to:(comma-separated): ").split(',')
        class_number = [int(c) for c in class_number]
        task_subject = input("Enter the subject of the task: ")
        task_details = input("Enter the details of the task: ")
        task_due_date = input("Enter the due date for the task (YYYY-MM-DD): ")

        task_key = f"ca{class_number}_grade_{grade_number}"
        if task_key not in tasks:
            tasks[task_key] = []

        tasks[task_key].append({
            'subject': task_subject,
            'details': task_details,
            'due_date': task_due_date,
            'completed': False
        })

        # Save tasks to JSON file
        with open("tasks.json", "w") as json_file:
            json.dump(tasks, json_file)


def display_teacher_tasks(teacher_name, teacher_email):
    for key, value in tasks.items():
        if key.startswith(f"{teacher_name}_{teacher_email}"):
            print("Tasks given by you:")
            for idx, task in enumerate(value, start=1):
                print(f"Task {idx}:")
                print(f"Subject: {task['subject']}")
                print(f"Details: {task['details']}")
                print(f"Due Date: {task['due_date']}")
                print()
def add_task_for_student(student_name):
    student_tasks = tasks.get(student_name, [])
    task_subject = input("Enter the subject of the task: ")
    task_details = input("Enter the details of the task: ")
    task_due_date = input("Enter the due date for the task (YYYY-MM-DD): ")

    student_tasks.append({
        'subject': task_subject,
        'details': task_details,
        'due_date': task_due_date,
        'completed': False
    })

    # Save tasks to JSON file
    with open("tasks.json", "w") as json_file:
        json.dump(tasks, json_file)


def mark_task_as_completed(student_name):
    student_tasks = tasks.get(student_name, [])
    if student_tasks:
        print("Your tasks:")
        for idx, task in enumerate(student_tasks, start=1):
            print(f"Task {idx}:")
            print(f"Subject: {task['subject']}")
            print(f"Details: {task['details']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Completed: {'Yes' if task['completed'] else 'No'}")
        task_number = int(input("Enter the number of the task you want to mark as completed: "))
        if 1 <= task_number <= len(student_tasks):
            student_tasks[task_number - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    else:
        print("You have no tasks assigned.")

    # Save tasks to JSON file
    with open("tasks.json", "w") as json_file:
        json.dump(tasks, json_file)


def display_completed_tasks(student_name):
    student_tasks = tasks.get(student_name, [])
    if student_tasks:
        completed_tasks = [task for task in student_tasks if task['completed']]
        if completed_tasks:
            print("Completed tasks:")
            for idx, task in enumerate(completed_tasks, start=1):
                print(f"Task {idx}:")
                print(f"Subject: {task['subject']}")
                print(f"Details: {task['details']}")
                print(f"Due Date: {task['due_date']}")
        else:
            print("You have no completed tasks.")
    else:
        print("You have no tasks assigned.")


def display_tasks(student_name):
    student_tasks = tasks.get(student_name, [])
    teacher_tasks = []
    for key, value in tasks.items():
        if key.startswith('ca'):
            teacher_tasks.extend(value)
    all_tasks = student_tasks + teacher_tasks
    if all_tasks:
        print("All Tasks:")
        for idx, task in enumerate(all_tasks, start=1):
            print(f"Task {idx}:")
            print(f"Subject: {task['subject']}")
            print(f"Details: {task['details']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Completed: {'Yes' if task['completed'] else 'No'}")
    else:
        print("You have no tasks assigned.")


def display_schedule(student_name):
    student_info = users_info.get(student_name, {})
    if student_info:
        schedule = student_info.get('schedule', {})
        if schedule:
            print("Your Schedule:")
            for day, classes in schedule.items():
                print(day)
                for hour, subject in classes.items():
                    print(f"{hour}: {subject}")
        else:
            print("You have no schedule.")
    else:
        print("No information found for this student.")




def main():
    global users_info, tasks
    users_info = load_users_info()
    tasks = load_tasks()

    print("\nWelcome to the Task Management System!")

    while True:
        user_type = input("\nAre you a teacher or a student? (Type 'teacher' or 'student', or 'exit' to quit): ")
        if user_type.lower() == "teacher":
            option = 0
            while (option != 3):
                teacher_info()
                print("\nChoose an option:")
                print("1. Add a task")
                print("2. See all tasks")
                print("3. Exit")
                option = input("Enter your choice (1/2/3): ")
                if option == "1":
                    add_task_for_teacher()
                elif option == "2":
                    display_teacher_tasks(teacher_name, teacher_email)
                elif option == "3":
                    print("Exiting.")
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 6.")

        elif user_type.lower() == "student":
            student_name = input("Enter your name: ")
            if student_name not in users_info:
                print("You need to provide some additional information to proceed.")
                email = input("Enter your email address: ")
                grade = input("Enter your grade: ")
                class_number = input("Enter your class number: ")
                schedule = {}
                days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                for day in days:
                    schedule[day] = {}
                    for hour in range(11):
                        subject = input(f"Enter the subject for {day} at hour {hour}: ")
                        schedule[day][hour] = subject
                # Save student information
                save_user_info(student_name, email, 'student', {'grade': grade, 'class_number': class_number, 'schedule': schedule})

            option = 0
            while (option != 6):
                print("\nChoose an option:")
                print("1. Add a task")
                print("2. Mark task as completed")
                print("3. See completed tasks")
                print("4. See schedule")
                print("5. See all tasks")
                print("6. Exit")
                option = input("Enter your choice (1/2/3/4/5/6): ")
                if option == "1":
                    add_task_for_student(student_name)
                elif option == "2":
                    mark_task_as_completed(student_name)
                elif option == "3":
                    display_completed_tasks(student_name)
                elif option == "4":
                    display_schedule(student_name)
                elif option == "5":
                    display_tasks(student_name)
                elif option == "6":
                    print("Exiting.")
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 6.")
            elif user_type.lower() == "exit":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 'teacher', 'student', or 'exit'.")


if __name__ == "__main__":
    main()

