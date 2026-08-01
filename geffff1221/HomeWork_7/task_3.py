word = input("Enter a word: ")
my_dictrionary = {a: word.count(a) for a in word}
print(my_dictrionary)