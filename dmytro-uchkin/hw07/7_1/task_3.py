"""
    Task3. Write a function that calculates the number of characters included in given string

    input: "hello"
    output: {"h":1, "e":1, "l":2, "o":1}
"""

def count_character_inclusions(input_string):
    """Count the number of characters included in given string"""

    result = {}

    for character in input_string:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1

    return result


def handle_user_prompt():
    """
     Ask the user for a string to calculate the number of characters included in it
    """

    input_str = input("Enter a string to calculate the number of characters included in it: ")

    print(f"The given string includes: {count_character_inclusions(input_str)}")

while True:
    handle_user_prompt()