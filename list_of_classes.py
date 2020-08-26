
# Create an empty list
class_list = []

# Begin with add_class prompt
add_class = input("Would you like to add a class to your list? Y/N")

# Prompting for class names until NO
while add_class.upper() == "Y":
    # Display class_name input
    class_name = input("Please enter class name: ")
    # Add class to list
    class_list.append(class_name)
    # Prompt for another class
    add_class = input("Would you like to add a class to your list? Y/N")

# Display list
for class_name in class_list: # https://stackoverflow.com/questions/13443588/how-can-i-format-a-list-to-print-each-element-on-a-separate-line-in-python
    # Sort the list
    class_list.sort()
    # Display the list
    print(class_name)