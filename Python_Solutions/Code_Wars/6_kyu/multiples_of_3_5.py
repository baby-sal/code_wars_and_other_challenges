"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)"""

def solution(number):
    list = [item for item in range(number)]
    result = 0
    for num in list:
        if num %3 == 0:
            result += num
        elif num%3 == 0 and num%5 == 0:
            result += 0
        elif num %5 == 0:
            result += num
    return result





print(solution(10))
print(solution(24))