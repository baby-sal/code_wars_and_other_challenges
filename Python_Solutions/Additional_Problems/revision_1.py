#Question 1
# egg_boxes = 4
# eggs_per_box = '8'
# total_eggs = egg_boxes * eggs_per_box
# message = 'I have {} eggs'.format(total_eggs)print(message)

#Problem 1 - The variable eggs_per_box is defined as a string, this should be changed
# into an 8, without inverted commas.
#Problem 2 - The print function should be moved to the next line.
#Problem 3 - The biggest problem is that this is not scalable. It should be made into a
#function that accepts egg_boxes as an argument, so that you can
#call the function with only the number of egg boxes. This will be more efficient.

#Question 2:
# hello_world()
# def hello_world():
#     print("hello world")

#The error is a name error. This is because the function has been called before
#it has been defined. Calling the function after it has been defined will fix this.

#Question 3
# def calculate_vat(amount):
#     return amount * 1.2
# calculate_vat(100)

#The problem is that boss is calling the function but as it 'returns' the result,
#the end user cannot see. Boss needs to print() the called function like print(calculate_vat(120)
#The result returned will have a decimal place so will also need to cast the result an int.
#I'd do this by amending the 2nd line of the func to return int(amount * 1.2).

#Question 4:
# for number in range(50):
#     print("50" * number)

#This program runs a for loop for the numbers in the range 0 - 50. That means
# for every number between 0 - 50 inclusive (in increments of 1) the program will
# iterate over them and run the block of code on it. In this case, that is to multiply the string "50" by
# the integer called in that loop and print the result (which will happen on a new line).
# Thus, the number 50 will be repeated x amount of times and the final result will be every
# iteration of the loop.

#Question 5:

# Task 1 - Slice the word so that you get "work".
# wrd="Homework"
# Type your answer here.
# ans_1= wrd[4:8]
# print(ans_1)
# # Task 2 - Slice the word until "w". (Home)
# wrd="Homework"
# # Type your answer here.
# ans_1=wrd[0:4]
# print(ans_1)
# Task 3 - Now try to get "me" only.
# wrd="Homework"
# # Type your answer here.
# ans_1=wrd[2:4]
# print(ans_1)
# Task 4 - Now slice the word with steps of 2, excluding first and last characters
# wrd="Homework"
# # Type your answer here.
# ans_1= wrd[1:-1:2]
# print(ans_1)

#
# Question 6:
# Write a function that takes in a string, and prints out the following:
# ● The string in uppercase
# ● The string in lowercase
# ● Whether the word starts with the same letter as the last letter
# ● The string with all instances of the first letter replaced with “[REDACTED]”
# For example:
# ● If “abcd” was the input, the function output would be:
# ABCD
# abcd
# False
# [REDACTED]bcd
#
# ● If “racecar” was the input, the function output would be:
# RACECAR
# racecar
# True
# [REDACTED]aceca[REDACTED] # both r’s are replaced

def function(a_string):
    uppercase_str = a_string.upper()
    print(uppercase_str)
    lowercase_str = a_string.lower()
    print(lowercase_str)
    first_letter = a_string[0].lower()
    last_letter = a_string[-1].lower()
    result = first_letter == last_letter
    print(result)
    for i in a_string:
        if i == first_letter:
            print(a_string.replace(i,"[REDACTED]"))

function("abcd")
function("racecar")