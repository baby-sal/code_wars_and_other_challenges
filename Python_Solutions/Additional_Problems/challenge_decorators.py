"""
Create a Decorator that tells you how long a function
has taken to run.

It should be called as @timer.

To do this, you'll need the `time` library imported.
the time library has many utilities within it,
consider using time.perf_counter(), but you may find another
alternative to this.

Maths hint:
To get the time between two moments,
subtract the start time away from the end time.

e.g:
I started timing at 16:36
I finished timing at 16:46

46 - 36 = 10
👆 a ten minute time difference.

However, your timer is going to be working with really
small time periods!
"""

# Test your timer against this long running function:
# With an input reasonably large, around 1000.
# Don't go too high of a number! You might be waiting a while!

import time

def timer(func):
    def inner_function(num):
        start = time.perf_counter()
        func(num)
        stop = time.perf_counter()
        return stop - start
    return inner_function

@timer
def worker_function_numbers(num):
    total_sum = 0
    for n in range(num):
        total_sum = total_sum + sum([(i/2 + 5) for i in range(1000)])
    return total_sum

print(worker_function_numbers(1000))
print(worker_function_numbers(500))