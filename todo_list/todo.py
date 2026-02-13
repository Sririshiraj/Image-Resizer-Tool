#!/usr/bin/env python3
"""
Console-based To-Do List Application
Persistent storage using a text file.
Author: Senior Dev Mode 😉
"""

from pathlib import Path
import sys

DATA_FILE = Path("tasks.txt")


class TodoApp:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    # -----------------------------
    # File Handling
    # -----------------------------
    def load_tasks(self):
        """Load tasks from file into memory."""
        if self.file_path.exists():
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        else:
            self.file_path.touch()

    def save_tasks(self):
        """Persist tasks to file."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")

    # -----------------------------
    # Core Features
    # -----------------------------
    def add_task(self, task: str):
        if not task.strip():
            print("⚠ Task cannot be empty.")
            return
        self.tasks.append(task.strip())
        self.save_tasks()
        print("✔ Task added successfully.")

    def remove_task(self, index: int):
        try:
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"🗑 Removed: {removed}")
        except IndexError:
            print("⚠ Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("\n📭 No tasks available.\n")
            return

        print("\n📌 Your Tasks:")
        print("-" * 30)
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
        print("-" * 30)

    # -----------------------------
    # CLI Loop
    # -----------------------------
    def run(self):
        while True:
            print("\n==== TO-DO LIST MENU ====")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Remove Task")
            print("4. Exit")

            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                self.view_tasks()

            elif choice == "2":
                task = input("Enter new task: ")
                self.add_task(task)

            elif choice == "3":
                self.view_tasks()
                if self.tasks:
                    try:
                        index = int(input("Enter task number to remove: ")) - 1
                        self.remove_task(index)
                    except ValueError:
                        print("⚠ Please enter a valid number.")

            elif choice == "4":
                print("👋 Exiting To-Do App. Goodbye!")
                sys.exit(0)

            else:
                print("⚠ Invalid option. Please select 1-4.")


# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    app = TodoApp(DATA_FILE)
    app.run()
