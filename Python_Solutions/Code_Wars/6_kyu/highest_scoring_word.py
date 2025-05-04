"""separate into individual words, translate the letters into numbers, loop over and add, compare the values"""

def high(x):
    lst = x.split(" ")
    high_score = 0
    best_word = ""

    for word in lst:
        score = sum(ord(letter) - 96 for letter in word)
        if score > high_score:
            high_score = score
            best_word = word

    return best_word
        
        


        
        
        
# number = ord(character) - 96
#             output.append(number)
    



print(high("man i need a taxi up to ubud"))
print(high("take me to semynak"))