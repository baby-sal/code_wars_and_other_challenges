"""Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd)."""

from collections import Counter

def find_it(seq):
    count_dict = Counter(seq)
    # print(count_dict)
    values = count_dict.values()
    # print(values)
    keys = count_dict.keys()
    result = []
    for i in values:
        if i %2 != 0:
            result.append(keys)
    return result




print(find_it([7]))
# print(find_it(["geeks", "for", "geeks"]))
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))