# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task for today: ")
priority = input("What is the priority of this task? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Start with a base message
reminder = f"Reminder: {task} - Priority: {priority.capitalize()}"

# Match-case to customize based on priority
match priority:
    case "high":
        reminder += ". This is a high-priority task!"
    case "medium":
        reminder += ". This is a medium-priority task. Try to complete it soon."
    case "low":
        reminder += ". This is a low-priority task. Plan accordingly."
    case _:
        reminder += ". Priority level is unrecognized."

# Add urgency if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final customized reminder
print(reminder)
