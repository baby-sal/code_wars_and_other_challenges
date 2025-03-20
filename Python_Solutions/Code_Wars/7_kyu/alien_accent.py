def convert(st):
    accent = st.maketrans({"a":"o", "o":"u"})
    return st.translate(accent)
        

print(convert("hello"))
print(convert("codewars"))