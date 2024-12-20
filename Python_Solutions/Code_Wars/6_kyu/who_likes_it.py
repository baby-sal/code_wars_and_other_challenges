# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(names):
    if not names:
        return "no one likes this"
    for i in names:
        if len(names) == 1:
            return f"{i} likes this"
        elif len(names) == 2:
            return f"{names[0]} and {names[1]} like this"
        elif len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        else:
            return f"{names[0]}, {names[1]} and " + str(len(names)-2) +  " others like this"


if __name__ == "__main__":
    print(likes([]))
    print(likes(["Peter"]))
    print(likes(["Peter", "Alex"]))
    print(likes(["Max", "John", "Mark"]))
    print(likes(["Alex", "Jacob", "Mark", "Max"]))
    print(likes(["Alex", "Jacob", "Mark", "Max","Peter", "Alex","Peter", "Alex"]))

# best practice other solution found on CodeWars:
# used a dictionary:
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)