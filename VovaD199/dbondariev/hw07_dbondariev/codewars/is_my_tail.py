correct_tail = lambda body, tail: body[-1] == tail

print(correct_tail("Fox", "x"))
print(correct_tail("Dog", "g"))
print(correct_tail("Cat", "t"))
print(correct_tail("Elephant", "t"))