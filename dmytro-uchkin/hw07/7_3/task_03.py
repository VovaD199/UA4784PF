"""
    Write a function taking in a string like "WOW this is REALLY          amazing" and returning "Wow this is really amazing".
    String should be capitalized and properly spaced.

    Examples:
        "HELLO CAN YOU HEAR ME" --> "Hello can you hear me"
        "now THIS is REALLY interesting" --> "Now this is really interesting"
        "THAT was EXTRAORDINARY!" --> "That was extraordinary!"
"""

user_string: str = input()


def filter_words(st: str):
    lower_case_string = st.lower().capitalize()
    split_string = lower_case_string.split(" ")

    return " ".join([st for st in split_string if st != ""])


filter_words(user_string)
