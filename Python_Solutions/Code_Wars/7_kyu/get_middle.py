import math
def get_middle(s):
    lst = []
    for index, letter in enumerate(s):
        if len(s) % 2 == 0:
            lst.append(letter[len(s) / 2])
        else:
            lst.append


print(get_middle("test"))
print(get_middle("testing"))