def solution(s):
    new_s = ""
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_s += " " + i
        else:
            new_s += i
    return new_s



print(solution("helloWorld"))
print(solution("camelCasing"))  

""" one line sol def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
    """