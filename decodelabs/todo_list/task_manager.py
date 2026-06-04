import json
import os
from datetime import datetime

# Define the file name where tasks will be stored
DB_FILE = "tasks.json"

def load_tasks():
    """
    CONCEPT: File Handling & JSON
    Loads tasks from a JSON file. If the file doesn't exist, it returns an empty list.
    Exception handling is used to manage potential file errors.
    """
    if not os.path.exists(DB_FILE):
        return []
    
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        # If file is corrupted or unreadable, start fresh
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """
    CONCEPT: Persistence
    Saves the list of dictionaries into a JSON file for data persistence.
    """
    try:
        with open(DB_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks, name, priority):
    """
    CONCEPT: Data Structures (Dictionaries)
    Adds a new task object to the list. 
    Each task is a dictionary for structured data access.
    """
    # Generating a unique ID based on existing tasks
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    
    new_task = {
        "id": new_id,
        "name": name,
        "priority": priority,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def mark_completed(tasks, task_id):
    """
    CONCEPT: List Traversal & Modification
    Finds a task by ID and updates its status.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "Completed"
            save_tasks(tasks)
            return True
    return False

def delete_task(tasks, task_id):
    """
    CONCEPT: List Comprehension / Filtering
    Removes a task from the list based on its ID.
    """
    original_count = len(tasks)
    # Using list comprehension to create a new list without the target task
    tasks[:] = [t for t in tasks if t['id'] != task_id]
    
    if len(tasks) < original_count:
        save_tasks(tasks)
        return True
    return False

def search_tasks(tasks, query):
    """
    CONCEPT: String Manipulation & Filtering
    Returns tasks where the name matches the search query.
    """
    # Case-insensitive search
    return [t for t in tasks if query.lower() in t['name'].lower()]
