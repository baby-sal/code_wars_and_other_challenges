# A dictionary called items_info that contains information about the items and their prices.
# A dictionary called sales_info that contains information about the quantities sold for each item.

#EXample input
# contains the price of said item as the value.
items_info = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.7,
    "grape": 1.2
}
#Sales_Info contains the quantity of said item as the value.
sales_info = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 12
}
#Example output : 26.5
# Calculate the revenue using the following formula:
# revenue = quantity * price
# Also create a comprehensive test suite (that contains at least a success case, failure case, and edge case).

def total_revenue(dict_1,dict_2):
    total_rev = sum(dict_1[k]*dict_2[k] for k in dict_1)
    return total_rev

print(total_revenue({"apple": 500,
    "banana": 300,
    "orange": 700,
    "grape": 1200
},{
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 12
}, ))