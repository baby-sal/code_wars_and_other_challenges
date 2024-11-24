def animal_function(func):
    def inner_wrapper():
        print("My favourite animal is")
        func()
    return inner_wrapper

@animal_function
def another_function():
    print("dogs")

another_function()