# Calculator Class
class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    # Static Method: Adds two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method: Multiplies two numbers
    @classmethod
    def multiply(cls, a, b):
        # Accessing the class attribute calculation_type with lowercase "type"
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Main function to demonstrate usage
def main():
    # Using the static method to add two numbers
    result_add = Calculator.add(10, 5)
    print(f"The sum is: {result_add}")

    # Using the class method to multiply two numbers
    result_multiply = Calculator.multiply(10, 5)
    print(f"The product is: {result_multiply}")

if __name__ == "__main__":
    main()
