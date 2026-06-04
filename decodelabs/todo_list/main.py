import sys
import os
from colorama import Fore, Style, init
from task_manager import load_tasks, add_task, mark_completed, delete_task, search_tasks

# Initialize colorama for cross-platform terminal colors
init(autoreset=True)

def clear_screen():
    """Clears the terminal screen for a clean UI experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """Displays a professional ASCII banner."""
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║   _____ ___     ____   ___     _     ___ ____ _____  ║
  ║  |_   _/ _ \   |  _ \ / _ \   | |   |_ _/ ___|_   _| ║
  ║    | || | | |  | | | | | | |  | |    | |\___ \ | |   ║
  ║    | || |_| |  | |_| | |_| |  | |___ | | ___) || |   ║
  ║    |_| \___/   |____/ \___/   |_____|___|____/ |_|   ║
  ║                                                      ║
  ║           TO-DO LIST & TASK MANAGEMENT               ║
  ╚══════════════════════════════════════════════════════╝
"""
    print(banner)

def display_tasks(tasks, title="YOUR TASKS"):
    """
    CONCEPT: Loops & Enumerate
    Pretty-prints the task list in a tabular format.
    """
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}--- {title} ---")
    if not tasks:
        print(f"{Fore.RED}No tasks found.")
        return

    # Header
    print(f"{'ID':<4} {'Task Name':<30} {'Priority':<10} {'Status':<12} {'Created At'}")
    print("-" * 75)

    for task in tasks:
        # Color coding based on status and priority
        status_color = Fore.GREEN if task['status'] == "Completed" else Fore.YELLOW
        priority_color = Fore.RED if task['priority'] == "High" else (Fore.BLUE if task['priority'] == "Medium" else Fore.WHITE)
        
        print(f"{task['id']:<4} {task['name']:<30} {priority_color}{task['priority']:<10}{Style.RESET_ALL} {status_color}{task['status']:<12}{Style.RESET_ALL} {task['created_at']}")

def get_valid_input(prompt, options=None):
    """
    CONCEPT: Input Validation
    Ensures user provides valid input from a set of options or non-empty strings.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(f"{Fore.RED}Input cannot be empty!")
            continue
        if options and user_input not in options:
            print(f"{Fore.RED}Invalid option! Choose from: {', '.join(options)}")
            continue
        return user_input

def main():
    tasks = load_tasks()
    
    while True:
        clear_screen()
        show_banner()
        
        print(f"{Fore.GREEN}1. View Tasks")
        print(f"{Fore.GREEN}2. Add Task")
        print(f"{Fore.GREEN}3. Mark Task Completed")
        print(f"{Fore.GREEN}4. Delete Task")
        print(f"{Fore.GREEN}5. Search Task")
        print(f"{Fore.RED}6. Exit")
        
        choice = input(f"\n{Fore.WHITE}{Style.BRIGHT}Select an option (1-6): ").strip()
        
        try:
            if choice == '1':
                display_tasks(tasks)
                input(f"\n{Fore.CYAN}Press Enter to return to menu...")
            
            elif choice == '2':
                name = get_valid_input("Enter task name: ")
                priority = get_valid_input("Enter priority (High/Medium/Low): ", ["High", "Medium", "Low"])
                add_task(tasks, name, priority)
                print(f"\n{Fore.GREEN}Task added successfully!")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                
            elif choice == '3':
                display_tasks(tasks)
                task_id = int(get_valid_input("Enter Task ID to complete: "))
                if mark_completed(tasks, task_id):
                    print(f"\n{Fore.GREEN}Task marked as completed!")
                else:
                    print(f"\n{Fore.RED}Task ID not found.")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                
            elif choice == '4':
                display_tasks(tasks)
                task_id = int(get_valid_input("Enter Task ID to delete: "))
                if delete_task(tasks, task_id):
                    print(f"\n{Fore.GREEN}Task deleted successfully!")
                else:
                    print(f"\n{Fore.RED}Task ID not found.")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                
            elif choice == '5':
                query = get_valid_input("Search for: ")
                results = search_tasks(tasks, query)
                display_tasks(results, f"SEARCH RESULTS FOR '{query}'")
                input(f"\n{Fore.CYAN}Press Enter to return to menu...")
                
            elif choice == '6':
                print(f"\n{Fore.YELLOW}Saving tasks and exiting. Goodbye!")
                break
            
            else:
                print(f"{Fore.RED}Invalid selection. Please try again.")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                
        except ValueError:
            print(f"\n{Fore.RED}Error: Please enter a valid numerical ID.")
            input(f"\n{Fore.CYAN}Press Enter to continue...")
        except Exception as e:
            print(f"\n{Fore.RED}An unexpected error occurred: {e}")
            input(f"\n{Fore.CYAN}Press Enter to continue...")

if __name__ == "__main__":
    main()
