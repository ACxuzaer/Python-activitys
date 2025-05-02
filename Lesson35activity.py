from datetime import date , time , datetime


# calling the today
# funtion of date class
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Date and time is ", now)


# Printting date's components
print("\nDate components", today.year, today.month, today.day)