"""
TASK 1
Write a function that accepts a string and returns True if string is palindromic, False otherwise.

Extra: Write at least 3 unit tests for this function
"""
##sanitize the input

def palindrome_check(str: str) -> bool:
    if str == str[::-1]:
        return True
    else:
        return False
    # rev = ''.join(reversed(str))
    #
    # # Checking if both string are
    # # equal or not
    # if (str == rev):
    #     return True
    # return False

# print(palindrome_check("hannah"))