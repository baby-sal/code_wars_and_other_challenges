def sortedSquaredArray(array):
    new_arr = []
    for i in array:
        j = i**2
        new_arr.append(j)
    return sorted(new_arr)


print(sortedSquaredArray([1,2,3,4,5,6,7,8,9]))
print(sortedSquaredArray([-1,1,2,3]))
print(sortedSquaredArray([0]))