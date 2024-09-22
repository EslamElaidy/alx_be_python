# Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table
Y_list = range(1, 11)

for y in Y_list:  # Added the colon here
    product = number * y
    print(f"{number} * {y} = {product}")
