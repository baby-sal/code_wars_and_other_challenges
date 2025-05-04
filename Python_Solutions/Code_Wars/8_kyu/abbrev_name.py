def abbrev_name(name):
    x, y = name.split()
    return f"{x[0].upper()}.{y[0].upper()}"
   

print(abbrev_name("Sally Davies"))


# def abbrevName(name):
#     first, last = name.upper().split(' ')
#     return first[0] + '.' + last[0]