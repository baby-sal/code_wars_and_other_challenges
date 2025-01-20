"""Write a function, which takes a non-negative integer 
(seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures."""


def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - (h * 3600) - (m * 60)
    return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"


print(make_readable(60))
print(make_readable(3599))
    

"""0>2d:

0: Specifies that the padding character is 0. If the value is shorter than 2 digits, 0 will be added to the left to make it 2 digits.
>: Specifies right alignment. The value will be padded from the left, so the digits are aligned to the right in the space of 2 characters.
2: Indicates the minimum width of the field. If the value has fewer than 2 characters, it will be padded to meet this width.
d: Means the value is treated as a decimal integer."""