tasks = []

# Function to save tasks into the program's code
def save_tasks():
    global tasks
    tasks_code = f"tasks = {tasks!r}"
    with open(__file__, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for idx, line in enumerate(lines):
        if line.startswith("tasks ="):
            lines[idx] = tasks_code + '\n'
            break
    else:
        lines.insert(0, tasks_code + '\n')
    with open(__file__, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# A function to help the user understand the program:
def user_help():
    print('''\033[0;33m
[h] -->  help you for understand app
[a] -->  enter your task
[q] -->  back to mean menu
[s] -->  show all your task
[d] -->  delete your task
[m] -->  Mark the task as done
[u] -->  unmark the task as done
        \033[0m\n''')

# A function to add new tasks:
def add_tasks():
    while True:
        task = input('Enter your task: ')
        tasks.append(task)

        if task == 'q':
            del tasks[-1]
            break
    save_tasks()

# A function to show all tasks:
def show_tasks():
    if not tasks:
        print('\033[0;30mNo tasks\033[0m')
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'\033[0;32m{idx}. {task}\033[0m')

# A function to delete tasks:
def delet_tasks():
    delet = int(input('\033[0;35mEnter the number of the task you want to delete or [0] to delete all tasks: \033[0m'))
    if delet == 0:
        tasks.clear()
        print('\033[0;34mAll tasks deleted!\033[0m')
    elif delet > len(tasks):
        print('\033[0;31mNo task with this number\033[0m')
    else:
        del tasks[delet-1]
    save_tasks()

# A function to mark tasks as done:
def mark_tasks():
    mark = int(input ('\033[0;35mEnter the number of the task you want to mark or [0] to mark all tasks: \033[0m'))
    if mark == 0:
        for i in range(len(tasks)):
            if '[●]' not in tasks[i]:
                tasks[i] += ' \033[0;33m[●]\033[0m'
        print('\033[0;34mAll tasks marked as done!\033[0m')
    elif mark > len(tasks):
        print('\033[0;31mNo task with this number\033[0m')
    else:
        if '[●]' not in tasks[mark-1]:
            tasks[mark-1] = tasks[mark-1] + ' \033[0;33m[●]\033[0m'
    save_tasks()

# A function to Unmarked tasks:
def Unmark_tasks():
    unmark = int(input ('\033[0;35mEnter the number of the task you want to unmark or [0] to unmark all tasks: \033[0m'))
    if unmark == 0:
        for i in range(len(tasks)):
            if '[●]' in tasks[i]:
                tasks[i] = tasks[i].replace('[●]', '', 1)
    elif unmark > len(tasks):
        print('\033[0;31mNo task with this number\033[0m')
    else:
        if '[●]' in tasks[unmark-1]:
            tasks[unmark-1] = tasks[unmark-1].replace('[●]','')
    save_tasks()


# Starting the program:
print('Welcome to the to-do list app')
print('-------------------------------')
print("\033[0;30mEnter 'h' to know how to use the app\033[0m\n")

# Initialize the task list
try:
    tasks  # Check if 'tasks' is already defined
except NameError:
    tasks = []

while True:
    want = input('\033[0;36mWhat i want: \033[0m')

    try:
        if want == 'h':
            user_help()
        elif want == 'a':
            add_tasks()
        elif want == 's':
            show_tasks()
        elif want == 'd':
            delet_tasks()
        elif want == 'm':
            mark_tasks()
        elif want == 'u':
            Unmark_tasks()
    except ValueError:
        print('\033[0;31mInvalid input. Please enter a number.\033[0m')