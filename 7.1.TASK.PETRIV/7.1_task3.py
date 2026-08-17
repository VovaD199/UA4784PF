word = input("Enter a word: ")

def count_letters(word):
    letter_count = {}

    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    return letter_count


print(count_letters(word))
