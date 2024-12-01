"""
THESE ARE THE KEY METHODS REQUIRED FOR A QUEUE:

push(item): Add an item to the top of the stack.
pop(): Remove and return the item from the top of the stack.
peek(): View the top item without removing it.
is_empty(): Check if the stack is empty.
is_full() (for limited stacks ONLY) - Check if the stack has reached its maximum size.
size(): Get the current number of items in the stack.

"""


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):

        if self.is_empty():
            return "Stack is empty."
        else:
            return "[Bottom] " + " -> ".join(map(str, self.stack)) + " [TOP]"

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


myStack = Stack()

myStack.push("Harry Potter 1")
myStack.push("Far from the Madding Crowd")
myStack.push("YOUR NEXT BOOK")

print(myStack)