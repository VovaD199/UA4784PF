my_sheep = [
    True, False, True, True, False,
    False, True, True, True, False,
    True, False, True, True, False,
]

count_sheep = lambda sheep: sheep.count(True)

print(count_sheep(my_sheep))