#To do list
####Functions to add
'''Functions to add:
    1. Add a task
    2. Delete the task
    3. Repeat the task
    4. View all tasks
    5. Mark as completed a task
    6. Delay the task
'''
"""Functions to be created:
    add_task
    delete_task
    repeat_task
    view_all_tasks
    mark_as_completed
    delay_task
"""
tasks = []
def add_task(tasks) :
     while True:
        task = input("Enter your task(or type done to stop): ")
        if task.lower()== 'done':
            break
        tasks.append(task)
        print("Your task is added!!")
add_task(tasks)
def view_all_tasks(tasks) :
    if len(tasks)==0:
        print("No task yet!!")
    else:
        print("Tasks to complete: ")
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")
view_all_tasks(tasks)
def mark_as_completed(tasks) :
        complete = int(input("Enter the completed task number: ")) - 1
        if complete <0 or complete >= len(tasks):
         print("Invalid task number!!")
        else:
         remove= tasks.pop(complete)
         print(f"Kudos!! {remove} is completed!!")
mark_as_completed(tasks)
view_all_tasks(tasks)
def repeat_task(tasks):
       repeat = int(input("Enter the task number to repeat: "))-1
       if repeat <0 or repeat >= len(tasks):
           print("Invalid task number!!")
       else:
           task_to_repeat = tasks[repeat]
           tasks.append(task_to_repeat)
           print(f"Wow!! Courage to '{task_to_repeat}' again")
repeat_task(tasks)
view_all_tasks(tasks)
def delete_task(tasks):
       delete = int(input("Enter the task number to delete: "))-1
       if delete <0 or delete >= len(tasks):
           print("Invalid Task number!!")
       else :
           dlt = tasks.pop(delete)
           print(f"Offo! Running away from {dlt} TT")
delete_task(tasks)
view_all_tasks(tasks)
def delay_task(tasks):
       delay = int(input("Enter the task number to delay: "))-1
       if delay <0 or delay >= len(tasks):
           print("Invalid Task number!!")
       else :
           delay_task = tasks.pop(delay)
           tasks.append(delay)
           print(f"You must complete {delay}!!")
delay_task(tasks)
view_all_tasks(tasks)