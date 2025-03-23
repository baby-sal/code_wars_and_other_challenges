from collections import Counter

def find_added(st1, st2):
    return "".join(sorted((Counter(st2) - Counter(st1)).elements()))
    

         
print(find_added("4455446", "447555446666"))
print(find_added("44554466", "447554466"))



# matches = str(set(lst1).intersection(lst2))

    # newlist = []
    # for i, value in enumerate(lst1):
    #     if lst1[i] != lst2[i]:
    #         newlist.append(value)

    # newlst = []

    # for a,b in zip(lst1, lst2):
    #     if a != b:
    #         newlst.append(b)