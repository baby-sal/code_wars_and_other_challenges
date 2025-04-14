def isValidSubsequence(array, sequence):
    p_array = 0
    p_seq = 0
    while p_array < len(array) and p_seq < len(sequence): #make sure in bounds of the arrays
        if array[p_array] == sequence[p_seq]: #if there is a match
            p_seq += 1
        p_array += 1
    return p_seq == len(sequence)
        

print(isValidSubsequence([1, 2, 3 ,4], [1, 3, 4]))
print(isValidSubsequence([1, 2, 3 ,4], [2, 4]))
print(isValidSubsequence([1, 2, 3 ,4], [5, 4]))

