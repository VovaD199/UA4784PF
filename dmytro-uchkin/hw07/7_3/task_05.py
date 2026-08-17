"""
    You need to write a function that reverses the words in a given string. Words are always separated by a single space.

    As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

    Example (Input --> Output)

        "Hello World" --> "World Hello"
        "Hi There." --> "There. Hi"
"""

user_string: str = input()


def reverse(st: str):
    split_str_list = st.strip().split(" ")
    split_str_list.reverse()

    return " ".join(split_str_list)


print(reverse(user_string))
