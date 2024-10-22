# Step 1: Create a function called encode()
# to replace all the lowercase vowels in a given string
# with numbers according to the following pattern:
#
# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4".
# There is no need to worry about uppercase vowels in this kata.
#
# Step 2: Now create a function called decode()
# to turn the numbers back into vowels according
# to the same pattern shown above.
#
# For example, decode("h3 th2r2") would return "hi there".
#
# For the sake of simplicity, you can assume that
# any numbers passed into the function will correspond to vowels.


def encode(st):
    return st.replace("a","1").replace("e", "2").replace("i","3").replace("o","4").replace("u","5")


def decode(st):
    return st.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u")

print(encode("hello"))
print(encode("sally davies"))
print(decode("h3 th2r2"))

#Other solution (best practice):
#def encode(s, t=str.maketrans("aeiou", "12345")):
#     return s.translate(t)
#
# def decode(s, t=str.maketrans("12345", "aeiou")):
#     return s.translate(t)