"""how to count occurences in a string using a dict"""

characters = {}

string = "hello my name is sally"

for char in string:
    characters[char] = characters.get(char, 0) + 1


print(characters)