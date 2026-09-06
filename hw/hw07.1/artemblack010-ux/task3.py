def count_characters(text):
    result = {}

    for char in text:
        result[char] = result.get(char, 0) + 1

    return result


text = input()
print(count_characters(text))