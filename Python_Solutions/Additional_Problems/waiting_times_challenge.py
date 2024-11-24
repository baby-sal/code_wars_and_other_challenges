def reduce_wait(x):
    x.sort()
    wait_time = 0
    for i in range(0, len(x)):
        wait_time += sum(x[:i])
    print(wait_time)


print(reduce_wait([ 3, 2, 1, 2, 6]))