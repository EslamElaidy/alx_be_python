FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = int(input("Enter the temperature to convert: "))
if temp_unit == "C":
    temp_in_C = convert_to_celsius(temp)
    print(f"{temp_in_C}")
elif temp_unit == "F":
    temp_in_F = convert_to_fahrenheit(temp)
    print(f"{temp_in_F}")
else:
    print("Invalid input")
