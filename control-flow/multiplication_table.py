number = int(input("Enter a number to see its multiplication table: "))
Y_list = range(1, 11)
for y in Y_list:
    print(f"{number} x {y} = {number * y}")
