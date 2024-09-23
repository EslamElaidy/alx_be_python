task = input("Enter task description")
priority = input("Enter task priority (high, medium, low): ")
time_bound = input("Is it time bound yes/no: ")
match priority:
case high:
if time_bound == "yes":
print("f{task} is a {priority} that requires immediate attention today!")
