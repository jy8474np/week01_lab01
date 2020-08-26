
# Date assistnace: https://discuss.codecademy.com/t/can-i-display-the-month-name-instead-of-a-number/337967
# and https://discuss.codecademy.com/t/can-i-display-the-month-name-instead-of-a-number/337967
# I feel like I was getting close-ish on "Happy birthday month" using datetime
# but I was getting too bogged down.

# from datetime import datetime

# Prompt user for "name" input
name = input("What's your name?")
# Prohibit leaving name input field blank
while len(name) == 0:
    # Display name input instructions
	print("Your name MUST contain ONE or more characters!")
    # Prompt again
	name = input("What's your name?")

# Prompt user for "name" input
birthday_month = input("What month were you born, " + name + "?")
# Prohibit leaving name input field blank
while len(birthday_month) == 0:
    # Display birthday_month field input instructions
	print("Your birth month MUST contain ONE or more characters!")
    # Prompt again
	month = input("What month were you born, " + name + "?")

# Display user greeting
print("Hi, " + name + "!")
# Display user name's character count
print("Did you know there are " + str(len(name)) + " characters in your name?")

# now = datetime.now()
# print(now.strftime('%B'))
