def safe_divide(numerator, denominator):
  try:
  numerator = float(numerator)
  denominator = float(denominator)
  result = numerator / denominator
except ZeroDivisionError:
  return "Error: Cannot divide by zero."
else:
return result
    
