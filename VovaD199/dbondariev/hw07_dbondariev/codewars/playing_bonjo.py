are_you_playing_banjo = lambda name: name + " plays banjo" if name[0].lower() == "r" else name + " does not play banjo"

print(are_you_playing_banjo("dima"))
print(are_you_playing_banjo("rambo"))