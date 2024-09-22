number = int(input("Enter a number to see its multiplication table: "))
X = number
Y_list = range(1, 11)
for Y in Y_list:
    Z = X * Y
    print(Z)
    print()
