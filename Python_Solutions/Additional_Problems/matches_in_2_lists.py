"""
__ Common Values __

Given two lists, example:
["Orange", 6, "Pizza", "Driver", 16, "Software Engineer"]
and
["Pluto", "Driver", 16, 6, "Hide",  "Reverse"]

Count the number of common values between.
- The values do not have to share the same index
- The values do have to be of the same type. For example, "15" (String) and 15 (Integer) are not the same.

"""
# def find_common_vals(a, b):
#     result = []
#     for i in a:
#         if i in b:
#             result.append(i)
#     return result

def find_common_vals(a, b):
    common = 0
    for i in a:
        if i in b:
            common += 1
    return common


if __name__ == "__main__":
    print(find_common_vals(["Orange", 6, "Pizza", "Driver", 16, "Software Engineer"],
["Pluto", "Driver", 16, 6, "Hide",  "Reverse"]))