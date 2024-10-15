def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        count = 0
        for n in range(a,b+1):
            count += n
        return count
    else:
        count = 0
        for n in range (a, b-1, -1):
            count += n
        return count


#other solutions:
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))