"""This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000]."""


from itertools import zip_longest

def solution(lst):
    sortd = list(set(sorted(lst)))
    compr = list(range(sortd[0],sortd[len(sortd)-1]))
    if sortd[len(sortd) - 1] < 0:
        return 1
    else:
        for a, b in zip_longest(sortd, compr):
            if a != b:
                c = compr.index(a-1)
                return compr[c]
            else:
                return (sortd[len(sortd) - 1] + 1)

    


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))