"""
Using the previous Even_Numbers Iterator,
Write an iterator that traverses through even
numbers, but when `.history` is called all
previous iterations are returned in a list.
Remember what you've previously learned about
classes and extend the existing code to fit this
criteria.
"""

"""
Using the previous Generator as an example,
write a Generator called "My_Fridge".
Each time the generator is called, it should read
out items you would find on that shelf of a fridge.

Return an object where the Key is the name of the
shelf, and the value is the list contents of that
shelf.
"""


# A simple generator function
def my_fridge():
    fridge = {1: "eggs", 2: "cheese", 3: "veggies"}
    n = 0
    yield fridge[n + 1]

    yield fridge[n + 2]

    yield fridge[n + 3]


g = my_fridge()
print(next(g)) # first
print(next(g)) # second
print(next(g)) # third