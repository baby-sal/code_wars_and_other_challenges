def xo(s):
    str = s.lower()
    xs = str.count("x")
    os = str.count("o")
    if xs == os:
        return True
    elif xs != os:
        return False
    else:
        return True
    
print(xo("ooxx"))
print(xo("xooxx"))
print(xo("zpzpzp"))