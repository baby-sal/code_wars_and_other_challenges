# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you
# an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes
# (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

def ten_minute_walk(walk):
    if len(walk) != 10:
        return False
    ew = 0
    ns = 0

    for i in walk:
        if i == "e":
            ew += 1
        if i == "w":
            ew -= 1
        if i == "n":
            ns += 1
        if i == "s":
            ns -= 1
    return ew == 0 and ns == 0


if __name__ == "__main__":
    print(ten_minute_walk(['n','n','n','s','n','s','n','s','n','w']))

# Other solution:
# def isValidWalk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')