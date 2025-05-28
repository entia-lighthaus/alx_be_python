# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task for today: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start with a base message
reminder = f"'{task}' is a {priority} priority task"

# Match-case to customize based on priority
match priority:
    case "high":
        reminder += ""
    case "medium":
        reminder += ""
    case "low":
        reminder += ""
    case _:
        reminder = f"Note: '{task}' has an unrecognized priority."

# If time-bound, add urgency
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", reminder)

