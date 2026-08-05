user_enter = str(input("Enter a word: "))
letter_count = {}
for letter in user_enter:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)