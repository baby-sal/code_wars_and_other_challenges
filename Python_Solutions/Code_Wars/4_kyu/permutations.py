"""In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']"""

from itertools import permutations as p

def permutations(s):
    lst =  list(p(s))
    lst2 =  [(''.join(str(i) for i in x)) for x in lst]
    lst3 = []
    for j in lst2:
        if j not in lst3:
            lst3.append(j)
        else:
            continue
    return lst3


#sol 2, better for time complexity
from itertools import permutations as p

def permutations(s):
    # Convert to list and count character frequencies
    lst = list(s)
    n = len(lst)
    
    # Use a set to avoid duplicates
    seen = set()
    for i in p(s):
        joined = ''.join(i)
        if joined not in seen:
            seen.add(joined)
            yield joined



print(permutations('a'))
print(permutations('ab'))
print(permutations('abc'))
print(permutations('aabb'))