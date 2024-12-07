"""Topic 1: Trees
8 marks

Question 1
Give three properties of a tree.
They contain nodes connected by edges. The first node is called the root node, the last node is called a leaf node.
The edges connect nodes. The nodes contain data and the edges point to the next node in the tree.
Acyclic

Question 2
What is the meaning of a k-nary tree?
A k-nary tree means that the nodes of the tree have at most 'k' child nodes.
A binary tree is a k-nary tree where k == 2

Question 3
What makes the tree on the right an efficient binary search tree?
The tree is balanced, which makes the sorting algorithm more efficient as the work is split evenly.

Question 4
Design the most inefficient binary search tree using the value nodes from the previous question. Explain why this would be inefficient.
Imbalanced binary tree.
Would be inefficient as a binary tree would split the work in half, which cannot do with a linked list.
"""


"""
Question 1
What is hashing?
Using a function or algorithm to map data to an integer value.

Question 2
What are the 3 functions a hash table has to support?
Get/Lookup - locates an element in a hash table
Insert - adds an element into the hash table
Delete - removes an element from the hash table

Question 3
What is it called when a value maps to an already occupied index?
hash collision

Question 4
What are 2 ways to deal with the issue described in Question 3?
using a linked list chaining to store data for that index
open addressing (finding another available spot)
"""

"""
Using the class diagram below, create a python file and make the classes and subclasses as described:
*Red text denotes abstract methods
*Blue text denotes implementing the abstract method to return the correct instance for that specific class
*For example, the perimeter of a right-angled triangle is equivalent to the height 
+ base + the hypotenuse (you will need to implement Pythagoras’ theorem to calculate)
*Methods need to return their value.
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calc_perimeter(self):
        pass

    @abstractmethod
    def calc_area(self):
        pass

class Square(Shape):
    def __init__(self,a):
        self.a = a

    def calc_perimeter(self):
        return self.a * 4

    def calc_area(self):
        return self.a * 2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        return (self.a * 2) + (self.b * 2)

    def calc_area(self):
        return self.a * self.b

class RightAngledTriangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def calc_perimeter(self):
        hyp = math.sqrt((self.height**2 + self.base**2))
        return hyp + self.height + self.base

    def calc_area(self):
        return (self.height * self.base) / 2

s = Square(6)
print(s.calc_perimeter())
# should get 24
print(s.calc_area())
# should get 36

r = Rectangle(6, 4)
print(r.calc_perimeter())
# should get 20
print(r.calc_area())
# should get 24

t = RightAngledTriangle(9,12)
print(t.calc_perimeter())
# should get 36
print(t.calc_area())
# should get 54
