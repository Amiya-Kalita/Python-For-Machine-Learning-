tasks = ["Pay bills", "Go grocery shopping", "Call the dentist", "Clean the car"]

print("Your To-Do List:")
# enumerate() gives us both the index (we'll start it at 1) and the task
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")