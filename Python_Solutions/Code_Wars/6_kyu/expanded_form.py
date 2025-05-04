def expanded_form(num):
    str_num = str(num)
    result = []
    for i, digit in enumerate(reversed(str_num)):
        if digit != "0":
            result.append(digit + ("0" * i))
    return " + ".join(reversed(result))


    

print(expanded_form(70003))


#Used the following for help:
# https://www.reddit.com/r/learnpython/comments/n9gi8g/function_to_convert_an_input_integer_into_its/