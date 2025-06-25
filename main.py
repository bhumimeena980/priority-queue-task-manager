import heapq
import json
import os

TASKS_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, priority, description):
        # Use negative priority because heapq is a min-heap by default
        heapq.heappush(self.tasks, (-priority, description))
        print(f"Task added: '{description}' with priority {priority}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("Tasks by priority:")
        # Sorted descending by priority
        for i, (priority, desc) in enumerate(sorted(self.tasks, reverse=True), 1):
            print(f"{i}. {desc} (Priority: {-priority})")

    def delete_task(self, index):
        try:
            sorted_tasks = sorted(self.tasks, reverse=True)
            task = sorted_tasks[index - 1]
            self.tasks.remove(task)
            heapq.heapify(self.tasks)
            print(f"Deleted task: '{task[1]}'")
        except IndexError:
            print("Invalid task number.")

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as f:
            json.dump([{"priority": -p, "description": d} for p, d in self.tasks], f)
        print("Tasks saved.")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                loaded = json.load(f)
                self.tasks = [(-task['priority'], task['description']) for task in loaded]
                heapq.heapify(self.tasks)
        else:
            self.tasks = []

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Save & Exit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            desc = input("Enter task description: ")
            while True:
                try:
                    prio = int(input("Enter priority (higher number = higher priority): "))
                    break
                except ValueError:
                    print("Please enter a valid integer.")
            manager.add_task(prio, desc)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.view_tasks()
            try:
                idx = int(input("Enter task number to delete: "))
                manager.delete_task(idx)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            manager.save_tasks()
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
