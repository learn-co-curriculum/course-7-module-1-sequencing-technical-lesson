def display_tasks(task_list):
    """Displays the list of tasks."""
    print("\nCurrent To-Do List:")
    for index, task in enumerate(task_list, start=1):
        print(f"\n{index}.{task}")

def filter_tasks(task_list, keyword):
    """Placeholder for filtering tasks (students will implement)."""
    filtered = [task for task in task_list if keyword.lower() in task.lower()]
    print(f"\nTasks matching '{keyword}': ")
    display_tasks(filtered)

def task_generator(task_list, keyword):
    """Placeholder for generator-based filtering (students will implement)."""
    return (task for task in task_list if keyword.lower() in task.lower())
    
