max_length = lambda x, y : len(max(x,y, key=len))

print(max_length("hello", "omg"))

create_set = lambda p, q : set(p + q)

print(create_set([1, 2, 3, 4], [2, 3, 5]))