:FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
  celsius = fahrenheit * 5/9
def convert_to_fahrenheit(celsius):
  fahrenheit = celsius * 9/5
temp_unit = int(input("press 1 for c and 2 for f"))
temp = int(input("Enter your degree"))
