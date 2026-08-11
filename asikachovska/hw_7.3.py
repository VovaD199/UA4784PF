text=input("Enter a word or text")
def count_characters(text):
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result
print(count_characters(text))