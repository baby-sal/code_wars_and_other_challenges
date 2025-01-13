"""A palindrome is a series of characters that read the same forwards as backwards,
 such as "hannah", "racecar" and "lol".

For this Kata, you need to write a function that takes a string of characters and 
returns the length, as an integer value, of the longest alphanumeric palindrome that 
can be formed by combining the characters in any order. You are free to use the characters 
as many times as it appears in that string. The function should not be case-sensitive.

For example:

Given "Hannah", the function should return 6.
Given "xyz__a_/b0110//a_zyx", the function should return 13, one possible 
alphanumeric palindrome is "xyza01b10azyx"."""

def longest_palindrome(s):
    filtered = "".join(i for i in s if i.isalnum())
    return filtered

print("absomd&*098()))")