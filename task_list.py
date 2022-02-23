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
            uncompleted_task_list.append(task["description"])
    print(uncompleted_task_list)

uncompleted_tasks(tasks)