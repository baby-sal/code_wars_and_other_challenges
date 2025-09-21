with open("programmingExpert.txt", "w") as f:
    for num in range(1,51):
        square = num**2
        f.write(str(square) + "\n")