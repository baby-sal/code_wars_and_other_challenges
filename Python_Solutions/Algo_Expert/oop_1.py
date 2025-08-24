class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


banana = Fruit("banana", 100)
apple = Fruit("apple", 300)

print(banana.name, banana.calories)
print(apple.name, apple.calories)