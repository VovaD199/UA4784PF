def count_chars(text):
    result = {}
    for char in text:
        result[char] = text.count(char)
    return result

print(count_chars("hello"))
