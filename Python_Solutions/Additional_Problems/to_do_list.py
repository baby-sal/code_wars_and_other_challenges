### EXERCISE 1 ###
"""
Create a to-do list program that writes user input
to a file

The program should:

Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to do item to the existing to-do items
Save the updated to-do items

NB: You will need to manually create a new file
# called todo.txt in the same folder as your program
before you start.
"""

print("Hello and welcome to your to do list")
print("\nPlease see your current list:")

file = open("/Users/sallydavies/PycharmProjects/codewarssolutions/Python_Solutions/Additional_Problems/test.txt", "r")
content = file.read()
print("\n" + content)

to_do = input("What do you want to add to the list?")

write_file = open("/Users/sallydavies/PycharmProjects/codewarssolutions/Python_Solutions/Additional_Problems/test.txt", "a+")
write_file.write("\n" + to_do)
write_file.close()
print("\nNew item added, please see new list")

new_file = open("/Users/sallydavies/PycharmProjects/codewarssolutions/Python_Solutions/Additional_Problems/test.txt", "r")
new_content = new_file.read()
print(new_content)