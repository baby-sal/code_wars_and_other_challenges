# print(5//2)

# for _ in range(10):
#     print("+" * _)

# Attempt 1:
# if cash_given / 2.0 > 2:
#     two_pous = int(cash_given/2.0)
#     cash_given = cash_given - 2.0*two_pous
# if cash_given / 1.0 > 6:
#     one_pous = int(cash_given/1.0)
#     cash_given = cash_given - *one_pous

# Attempt 2:
# for i in change_lst:
#     change = int(cash_given/change_lst)
#     change_lst.append(change)
#     cash_given = round(cash_given%change_lst,2)
# print(dict(change_lst))

# change_lst = cash_in_hand.items()

def petty_change(cash_given):
    cash_given_flo = float(cash_given)

    cash_in_hand = {
    0.01: 6,
    0.02: 4,
    0.05:7,
    0.1:6,
    0.2:4,
    0.5: 10,
    1.0: 6,
    2.0: 2
    }

    if cash_given_flo > 0:
        two_pous = cash_given_flo // 2
        one_pous = cash_given_flo % 2 // 1
        fifty_p = cash_given_flo % 2 % 1 // 0.5
        twenty_p = cash_given_flo % 2 % 1 % 0.5 // 0.2
        ten_p = cash_given_flo % 2 % 1 % 0.5 % 0.2 // 0.1
        five_p = cash_given_flo % 2 % 1 % 0.5 % 0.2 % 0.1 // 0.05
        two_p = cash_given_flo % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05 // 0.02
        one_p = cash_given_flo % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05 % 0.02 // 0.01

        change_taken = {
        0.01 : one_p,
        0.02 : two_p,
        0.05 : five_p,
        0.1 : ten_p,
        0.2 : twenty_p,
        0.5 : fifty_p,
        1.0 : one_pous,
        2.0 : two_pous
        }

        amount = [coin for coin in change_taken if coin in cash_in_hand.items()]

        if amount:
            print(amount)
        else:
            print("Can't afford this with the available petty change")
