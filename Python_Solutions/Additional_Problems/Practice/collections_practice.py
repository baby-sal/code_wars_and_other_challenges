"""counter"""
# from collections import Counter
# a = "aaaabbbbbbcccccc"
# a_counter = Counter(a)
# print(a_counter)
# print(a_counter.most_common(1))#list of tuples
# print(a_counter.most_common(1)[0][0])
# print(list(a_counter.elements()))

"""named tuple"""
# from collections import namedtuple
# Point = namedtuple("Point", "x,y")
# pt = Point(30,40)
# print(pt)
# print(pt.x, pt.y) #access the values

"""ordered dictionary, somewhat obsolete"""
# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict["a"] = 1
# ordered_dict["b"] = 2
# ordered_dict["c"] = 3
# print(ordered_dict)

"""default dict - will have a default value if it has not been set"""
# from collections import defaultdict
# d = defaultdict(int) #change the datatype to amend the default value
# d["a"] = 1
# d["b"] = 2
# print(d["a"])
# print(d["c"])

"""deque - used to add or remove elements from both ends"""
from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(2)

d.pop()

d.popleft()

d.clear() #deletes everything

d.extend([4,5,6]) #adds a list

d.extendleft([4,5,6]) # adds in reverse order

d.rotate(1) #rotates all elements one place to the right

d.rotate(-1)

print(d)