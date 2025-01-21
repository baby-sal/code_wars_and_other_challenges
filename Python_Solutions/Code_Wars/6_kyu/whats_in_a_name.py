"""What's in a name?
...Or rather, what's a name in? For us, a particular string is where we are looking for a name.

Task
Write a function, taking two strings in parameter, that tests whether or not the first string 
contains all of the letters of the second string, in order.

The function should return true if that is the case, and else false. Letter comparison 
should be case-INsensitive.

Examples
    "Across the rivers", "chris" --> true
      ^      ^  ^^   ^
      c      h  ri   s
                
    Contains all of the letters in "chris", in order.
----------------------------------------------------------
    "Next to a lake", "chris" --> false"""



# def name_in_str(strng : str, name : str) -> bool:
#    return(bool(set(strng).intersection(name)))
#Doesn't work because it doesn't check for order and is case sensitive


def name_in_str(strng: str, name: str) -> bool:
    strng = strng.lower()  # Ensure case insensitivity
    name = name.lower()
    
    # Create an iterator from the string
    it = iter(strng)
    
    # Check if all characters of 'name' are in the iterator of 'strng'
    return all(char in it for char in name)
    
print(name_in_str("Across the rivers", "chris"))

print(name_in_str("Under a sea", "chris"))

