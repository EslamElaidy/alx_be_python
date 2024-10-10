def safe_divide(numerator, denominator):
    try:
        # Nested try block to handle ValueError (non-numeric input)
            try:
                numerator = float(numerator)
                denominator = float(denominator)
            except ValueError:
                return "Error: Please enter numeric values only."
        
        # Perform the division (this can raise ZeroDivisionError)
        result = numerator / denominator
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    else:
        return f"The result of the division is {result:.1f}"

    
