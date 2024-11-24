def array_diff(a, b):
    my_list = []
    for y in a:
        if y not in b:
            my_list.insert((len(my_list)), y)
    return my_list

print(array_diff([1,2,3],[1,2]))
print(array_diff([1,2],[1]))
print(array_diff([1,2,2,2,3],[2]))

#Problem 1: the defined list 'my_list' was not carried through and was named 'new_list' in the if statement. You need to ensure
#that the variables you define are carried through, or they will have no meaning and crash the program.
#Problem 2: the function 'print's the result. Functions cannot print a result, they must 'return' the result. You can then print the called function after it has
#been defined. When you return a variable result, you don't need parentheses, so these can also be removed. --> return my_list
#Problem 3: The insert method requires two parameters; position (a number specifying which position to insert the value
# element (what you want to insert) can be any datatype.
#Problem 4: Following on, as we don't know the length of the list, we can't use an integer, so I have swapped it out for the len(my_list)
#which means whatever length my_list is, it will always insert y at the end.

#List comprehension can be used to clean up the code, as below.

def array_diff_2(a, b):
    my_list = [y for y in a if y not in b]
    return my_list

print(array_diff_2([1,2,3],[1,2]))
print(array_diff_2([1,2],[1]))
print(array_diff_2([1,2,2,2,3],[2]))