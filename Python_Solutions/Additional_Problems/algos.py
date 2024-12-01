# 1. Reverse Integer

# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverse(num):
    strng = str(num)
    for i in strng:
        if strng[0] == "-":
            no_minus = strng.replace("-", "")
            rev = no_minus[::-1]
            return int("-" + rev)
        else:
            return int(strng[::-1])


# print(reverse(-13456))
# print(reverse(12345))

###################################################################
# 2. First unique character

# Given an input string, find the first non-repeating character

def non_repeat(string):
    for i in string:
        if string.count(i) == 1:
            return i

print(non_repeat("aabccbdcbe"))