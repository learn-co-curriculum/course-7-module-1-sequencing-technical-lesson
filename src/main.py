from tasks.task_manager import display_tasks, filter_tasks, task_generator

# Initial list of tasks
tasks = ["Buy groceries","Work on Java Project", "Deploy React Project", "Buy fresh Groceries", "Finish project", "Call mom", "Send email", "Clean room"]

print("\nAll Tasks:")
display_tasks(tasks)
filter_tasks(tasks, "groceries")
# Creating a generator for "project" tasks
project_tasks = task_generator(tasks, "groceries")

# Retrieving tasks lazily
print(next(project_tasks))  # Output: 'Finish project'



