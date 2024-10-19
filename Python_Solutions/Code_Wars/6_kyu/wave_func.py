def wave(people: str) -> list:
    result = []
    for i in range(len(people)):
        if people[i].isalpha():
            wave = people[:i]+ people[i].upper() + people[1+i:]
            result.append(wave)
    return result

if __name__ == "__main__":
    print(wave("waveybaby"))
    print(wave("mood"))
    print(wave("1234"))
    print(wave("CAPITAL"))

