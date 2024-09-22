X = int(input("Enter a number to see its multiplication table: "))
Y_list = range(1, 11)
for Y in Y_list:  # Added the colon here
    Z = X * Y
    print(Z)
    print()
