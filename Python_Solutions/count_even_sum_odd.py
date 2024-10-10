def count_positives_sum_negatives(arr):
    if not arr:
        return []

    count_pos = 0
    sum_neg = 0
    for x in arr:
        if x > 0:
            count_pos += 1
        elif x < 0:
            sum_neg += x
    return [count_pos, sum_neg]