def count_characters(text):
    """Return a dictionary with character counts in the given string."""
    result = {}

    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


word = input("Enter word: ")
print(count_characters(word))
