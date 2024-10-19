def reverse_words(text):
    words = text.split(" ")
    nwords = []
    for word in words:
        return_string =""
        for c in reversed(word):
            return_string += c
        nwords.append(return_string)
    output_string = " ".join(nwords)
    return output_string

##or

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))