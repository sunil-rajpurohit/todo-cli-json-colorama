import os
import json
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

Task_File = "tasks.json"

#helper function

def load_tasks():
    if not os.path.exists(Task_File):
        return []
    with open(Task_File, "r") as file:
        return json.load(file)

#Saving Tasks to file
def save_tasks(tasks):
    with open(Task_File, "w") as file:
        json.dump(tasks, file, indent=4)

#clearing the screen for better CLI
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Displaying the task
def display_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "No tasks found.")
        return

    for idx, task in enumerate(tasks, start=1):
        if task["done"]:
            status = Fore.GREEN + "Task Completed"
            print(f"{idx}. {task['title']} - {status} - {task['timestamp']}")
        else:
            status = Fore.RED + "Pending"

            print(f"{idx}. {task['title']} - {status} - {task['timestamp']}")

#Adding the task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({
            'title': title,
            'done': False,
            'timestamp': datetime.now().strftime('%y-%m-%d %H:%M:%S')
            })

        save_tasks(tasks)
        print(Fore.GREEN + "Task added Successfully.")
        
#removing the task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: "))
        index-=1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(Fore.YELLOW + f"Removed Task: {removed['title']}")

    except ValueError:
        print(Fore.RED + "Invalid Input")


#marking the task
def mark_done(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: "))
        if 0 <= index < len(tasks):
            tasks[index]['done'] = not tasks[index]['done']
            save_tasks(tasks)
            status =  "Completed" if tasks[index]['done'] else "Pending"
            print(Fore.CYAN + f"Task marked as {status}")
    except ValueError:
        print(Fore.RED + "Invalid Input.")

#main function
def main():
    tasks = load_tasks()
    while True:
        clear_screen()
        print(Fore.BLUE + "===== TO-DO LIST =====")
        display_tasks(tasks)
        print("\n" + Fore.MAGENTA + "1.Add Task")
        print("2. Remove Task")
        print("3. Mark/Unmark Task")
        print("4. Exit : ")

        choice = input("\nChoose a option: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            print(Fore.GREEN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
            
                
            

        
