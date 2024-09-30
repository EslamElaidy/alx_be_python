from datetime import datetime, timedelta
def display_current_datetime()
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(current_date)
number_of_days = int(input("enter number of days"))
def calculate_future_date()
  added_days = timedelta(days=number_of_days)
  future_date = current_date + added_days
calculate_future_data()
print(future_date)
