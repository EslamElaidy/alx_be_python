def safe_divide(numerator, denominator):
  try:
  numerator = float(numerator)
  denominator = float(denominator)
  result = numerator / denominator
except ZeroDivisionError:
  return "Invalid number"
else:
return result
    
