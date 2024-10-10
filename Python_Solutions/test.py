def can_pay(price, cash_given):
    if cash_given >= price:
        return True
    else:
        return False


print(can_pay("five", 0))