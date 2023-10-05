from datetime import datetime, timedelta

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} ({status}) - Deadline: {self.deadline}"

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added successfully.")

    def view_upcoming_tasks(self):
        today = datetime.now()
        print("Upcoming Tasks:")
        for task in self.tasks:
            if not task.completed and task.deadline >= today:
                print(task)

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Task '{task.title}' marked as completed.")
                return
        print("Task not found.")

def main():
    task_scheduler = TaskScheduler()

    while True
