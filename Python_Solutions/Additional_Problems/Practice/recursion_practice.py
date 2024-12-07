# create fun called "walk" that takes in "step" as arg.
# get the rec fun to print out 0 to 10

def walk(step):
    print("Step:", step)

    if step == 10:
        return

    return walk(step + 1)

# print(walk(0))

"""Write a Python program to calculate the sum of a list of numbers using recursion."""

def sum_list(int_list):
    if len(int_list) == 1:
        return int_list[0]
    else:
        return int_list[0] + sum_list(int_list[1:])

# print(sum_list([2, 4, 5, 6, 7]))

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# print(factorial(5))


def fibonacci(num):
    if num ==1 or num==2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# print(fibonacci(7))