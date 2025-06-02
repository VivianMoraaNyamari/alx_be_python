"""
1. Prompt for a Single Task, Time Priority and Time-Bound
2. Process the Task Based on Priority and Time Sensitivity
3. Provide a Customized Reminder
"""

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes": 
         print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
         print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes": 
         print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
         print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes": 
         print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
         print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
         print(f"Invalid priority. Please enter high, medium or low")