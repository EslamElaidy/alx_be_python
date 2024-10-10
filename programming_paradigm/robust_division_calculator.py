def safe_divide(numerator, denominator):
  try:
    result = numerator / denominator
except ZeroDivisionError:
  return "Invalid number"
else:
return result
    
