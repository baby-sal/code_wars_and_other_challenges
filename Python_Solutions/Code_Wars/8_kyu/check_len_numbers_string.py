def validate_pin(pin):
    length = len(pin)
    numbers = pin.isdigit()
    if length == 4 and numbers == True:
        return True
    elif length == 6 and numbers == True:
        return True
    else:
        return False


    ## or

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()