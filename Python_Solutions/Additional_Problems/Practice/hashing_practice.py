def hash_func(lst):
    result = []
    for i in lst:
        result.append(i%10)
    return result



print(hash_func([4322, 1334, 1471, 9679, 1989, 6171, 6173, 4199]))