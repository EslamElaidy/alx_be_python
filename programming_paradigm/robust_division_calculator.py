def safe_divide(numerator, denominator):
  Try:
    result = numerator / denominator
except ZeroDivisionError:
  return "Invalid number"
else:
return result
    
