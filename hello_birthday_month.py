
# Date assistnace: https://discuss.codecademy.com/t/can-i-display-the-month-name-instead-of-a-number/337967
# and https://discuss.codecademy.com/t/can-i-display-the-month-name-instead-of-a-number/337967

# from datetime import datetime

name = input("What's your name?")
while len(name) == 0:
	print("Your name MUST contain ONE or more characters!")
	name = input("What's your name?")

birthday_month = input("What month were you born, " + name + "?")
while len(birthday_month) == 0:
	print("Your birth month MUST contain ONE or more characters!")
	month = input("What month were you born, " + name + "?")

print("Hi, " + name + "!")
print("Did you know there are " + str(len(name)) + " characters in your name?")

# now = datetime.now()
# print(now.strftime('%B'))
