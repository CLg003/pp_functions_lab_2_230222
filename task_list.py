
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Print a list of uncompleted tasks
def uncompleted_tasks(task_list):
    uncompleted_task_list = []
    for task in task_list:
        if task["completed"] == False:
            uncompleted_task_list.append(task)
    print(uncompleted_task_list)

# uncompleted_tasks(tasks)

# Print a list of completed tasks
def completed_tasks(task_list):
    completed_task_list = []
    for task in task_list:
        if task["completed"] == True:
            completed_task_list.append(task)
    print(completed_task_list)

# completed_tasks(tasks)

# Print a list of all task descriptions
def task_descriptions(task_list):
    task_description_list = []
    for task in task_list:
        task_description_list.append(task["description"])
    print(task_description_list)

# task_descriptions(tasks)

# Print a list of tasks where time_taken is at least a given time
def minimum_time(task_list):
    time = int(input("What is your minimum time? "))
    timed_tasks = []
    for task in task_list:
        if task["time_taken"] >= time:
            timed_tasks.append(task)
    
    print(timed_tasks)

# minimum_time(tasks)

# Print any task with a given description
def task_by_description(task_list):
    task_description = input("What task would you like to search for? ")
    for task in task_list:
        if task_description == task["description"]:
            print(task)
            break
# task_by_description(tasks)

# Given a description update that task to mark it as complete.
def mark_task_completed(task_list):
    task_description = input("What task have you completed? ")
    for task in task_list:
        if task_description == task["description"]:
            task["completed"] = True
            print(f"{task_description} task completed")

# mark_task_completed(tasks)

# Add a task to the list
def add_task(task_list):
    new_task = input("What task do you want to add? ")
    task_time = input("How long does it take? ")
    new_task = {"description" : new_task, "completed" : False, "time_taken" : task_time}
    task_list.append(new_task)
    print(f'{new_task["description"]} added to task list')

add_task(tasks)

# Use a while loop to display the following menu and allow the use to enter an option.
def display_menu():
    menu = ["Menu:", "1: Display All Tasks", "2: Display Uncompleted Tasks", "3: Display Completed Tasks", "4: Mark Task as Complete", "5: Get Tasks Which Take Longer THan a Given Time", "6: Find Task by Description", "7: Add a New Task to List", "M or m: Display This Menu", "Q or q: Quit"]
    menu_option = 0
    while menu_option < len(menu):
        print(menu[menu_option])
        menu_option += 1
    user_choice = input("Please select an option from the menu: ")
    return user_choice

# display_menu()

# Call the appropriate function depending on the users choice.
def do_task(user_choice):
    if user_choice == "1":
        task_descriptions(tasks)
    elif user_choice == "2":
        uncompleted_tasks(tasks)
    elif user_choice == 3:
        completed_tasks(tasks)
    elif user_choice == 4:
        mark_task_completed(tasks)
    elif user_choice == 5:
        minimum_time(tasks)
    elif user_choice == 6:
        task_by_description(tasks)
    elif user_choice == 7:
        add_task(tasks)
    




do_task(display_menu())