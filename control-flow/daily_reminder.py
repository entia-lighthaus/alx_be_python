# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = ""

# Process the task using match-case based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task. Try to complete it soon."
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"'{task}' has an unrecognized priority level."

# Modify reminder if time-bound and recognized priority
if priority in ["high", "medium", "low"] and time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the final customized reminder
print(reminder)
