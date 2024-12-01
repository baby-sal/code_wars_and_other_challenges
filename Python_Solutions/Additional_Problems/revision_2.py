#Question 1
# def sunglasses():
#     weather = input("Is it sunny today? (Y or N): ")
#     if weather == "Y":
#         print("Take your sunglasses.")
#     elif weather == "N":
#         print("You don't need sunglasses.")
#     else:
#         print("Invalid response.")
#
# if __name__ == "__main__":
#     sunglasses()

#Question 2
# my_money = input('How much money do you have? ')
# hour = 3
# venue cost = (200*hours) + 1.1
# if my_money < venue_cost:
#     print('You can afford the venue')
# else :
#     print('You cannot afford the venue'

#Problem 1 - the variable venue cost is two words separated by a space, when it is called later on, there is a
    #underscore.
#Problem 2 - the hour variable is called later as hours, should be amended
#Problem 3 - Missing parenthesis at the end of the last line
#Problem 4 - The program is supposed to return the hire cost + 10% deposit. Currently, it is adding
    #1.1 on line 3. Instead, the (200*hours) should be multiplied by 1.1
#Problem 5 - This can be made into a function so that the user can input the number of hours
    # and the function will return the result. It is more efficient.

# Question 3
# You work as a primary school teacher and are teaching numbers by showing how
# they are composed of units of ten and one. Write a program for students to play with
# to understand this concept. You will be asking for them to enter numbers between 1
# and 25 (they haven’t gone higher than that!), so you do not need to consider bigger
# numbers. The function needs to print to the screen and the message must be
# grammatically correct and in the format shown below.
# For example:
# ● If 15 was the input, the function output should be:
# One Ten, Five Ones
# ● If 21 was the input, the function output should be:
# Two Tens, One One
# ● If 20 was the input, the function output should be:
# Two Tens, Zero Ones
# ● If 8 was the input, the function output should be: