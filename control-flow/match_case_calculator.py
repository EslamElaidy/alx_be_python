num1 = float(input("Enter the first number:"))
num2 = float (input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
if operation == '/' and num2 == 0:
    print("Can't divide by zero")
else:
match operation:
case +:
print("the result is", num1 + num2)
case -:
print("the result is", num1 - num2)
case *:
print("the result is", num1 * num2)
case /:
print("the result is", num1 / num2)
