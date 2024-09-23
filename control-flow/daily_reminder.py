task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
case high:
if time_bound == "yes":
print("f{task} is a {priority} that requires immediate attention today!")
