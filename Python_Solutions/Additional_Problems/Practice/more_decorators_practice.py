"""Basic Decorator Implementation
Write a decorator print_message that prints "Function is being executed" before the execution of a function.

Decorator with Arguments
Write a decorator repeat that takes an integer n as an argument and repeats the execution of the decorated function n times.

Decorator for Timing
Write a decorator time_execution to measure the execution time of a function."""

"""Basic decorator implementation"""
# def message(func):
#     def inner_function():
#         print("Function is being executed")
#         func()
#     return inner_function
#
# @message
# def another_func():
#     print("decorator")
#
# another_func()

"""Decorator with arguments"""

# def repeat(n):
#     def inner_function(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_function
#
# @repeat(4)
# def another_func():
#     print("Hello")
#
# another_func()


"""Decorator for Timing"""

from time import time

def time_execution(func):
    def inner_function(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        stop = time()
        total = str(stop - start)
        print(f"Executed in {total}s")
        return result
    return inner_function()

@time_execution
def dog():
    print("Finished!")

print(dog)