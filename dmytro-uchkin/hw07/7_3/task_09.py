"""
    Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!

    The function takes a name as its only argument, and returns one of the following strings:

    name + " plays banjo" 
    name + " does not play banjo"

    Names given are always valid strings.
"""


def are_you_playing_banjo(name: str):
    return (
        name + " plays banjo"
        if name[:1].lower() == "r"
        else name + " does not play banjo"
    )


print(are_you_playing_banjo("martin"))  # martin does not play banjo
print(are_you_playing_banjo("Rikke"))  # Rikke plays banjo
print(are_you_playing_banjo("bravo"))  # bravo does not play banjo
print(are_you_playing_banjo("rolf"))  # rolf plays banjo
