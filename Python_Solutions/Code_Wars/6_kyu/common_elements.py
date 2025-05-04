"""they are present in both ones

they occur more than once in A and more than once in B

their values are within a given range (inclusive)

they are odd or even according as it is requested"""



def find_arr(arr_a, arr_b): #rng, wanted):
    both = (list(set(arr_a).intersection(arr_b)))
    count = {}
    for i in arr_a:
        count[i] = arr_b.count(i)
    return count

print(find_arr([1, -2, 7, 2, 1, 3, 7, 1, 0, 2, 3],[2, -1, 1, 1, 1, 1, 2, 3, 3, 7, 7, 0]))






# count = [[x,arr_a.count(x)] for x in set(arr_a)]


#import numpy as np
# common_elements = np.intersect1d(list1, list2)
# print(common_elements)