def are_you_playing_banjo(name):
    lower_name = name.lower()
    if lower_name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    

print(are_you_playing_banjo("Sally"))
print(are_you_playing_banjo("Rally"))
print(are_you_playing_banjo("rally"))