import datetime

# Define a variable for today's date and time
today = datetime.datetime.now()
print("Today is", today.strftime("%A, %B %d, %Y"))

# Define a variable for the user's birthday
birthday = datetime.date(1990, 5, 15)  # Example date, replace with actual birthday
print("My birthday is", birthday.strftime("%m/%d/%Y"))

# Define a variable for the date 90 days from today
ninety_d = today + datetime.timedelta(days=90)
print("90 days from today is", ninety_d.strftime("%B %d, %Y"))

# Define a variable for dinner time
dinner_time = datetime.time(19, 30)  # Example time at 7:30 PM
print("Let's meet for dinner at", dinner_time.strftime("%I:%M %p"))
