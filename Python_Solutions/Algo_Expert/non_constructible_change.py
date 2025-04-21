def nonConstructibleChange(coins):
    max_change = 0
    srt_coins = sorted(coins)
    if coins == []:
        return 1
    for coin in srt_coins:
        if coin > max_change + 1:
            return max_change + 1
        elif coin <= max_change + 1:
            max_change += coin
    return max_change + 1
        
print(nonConstructibleChange([]))
print(nonConstructibleChange([1,2]))
print(nonConstructibleChange([1,2,5]))
print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))