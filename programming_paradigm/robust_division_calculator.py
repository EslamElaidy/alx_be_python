def safe_divide(numerator, denominator):
  try:
    try:
    numerator = float(numerator)
    denominator = float(denominator)
  except ValueError:
    return "Error: Please enter numeric values only."
  result = numerator / denominator
except ZeroDivisionError:
  return "Error: Cannot divide by zero."
else:
return result
    
