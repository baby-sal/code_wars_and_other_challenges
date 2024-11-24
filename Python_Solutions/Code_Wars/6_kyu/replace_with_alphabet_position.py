def alphabet_position(text):
    text_lower = text.lower()
    output = []
    for character in text_lower:
        if character == " ":
            output += ""
        elif character == ".":
            output += ""
        elif character == ",":
            output += ""
        elif character == "'":
            output += ""
        else:
            number = ord(character) - 96
            output.append(number)
    return " ".join(str(i) for i in output)

print(alphabet_position("The sunset sets at twelve o' clock."))