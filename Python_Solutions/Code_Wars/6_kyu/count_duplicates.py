from collections import Counter

def duplicate_count(text):
    # new_list = [x for x in text if x in text]
    lwr_txt = text.lower()
    count = list()
    for char in lwr_txt:
        if char not in count and lwr_txt.count(char) > 1:
            count.append(char)
    return len(count)


if __name__ == "__main__":
    print(duplicate_count("mood"))
    print(duplicate_count("hhellooo"))
