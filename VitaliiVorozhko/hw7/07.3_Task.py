#Task 1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#Task 2

import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

#Task 3

def filter_words(st):
    return " ".join(st.lower().split()).capitalize()

#Task 4

def number_to_string(num):
    return str(num)

#Task 5

def reverse(st):
    return " ".join(st.split()[::-1])

#Task 6

def reverse_list(l):
    return l[::-1]

#Task 7

def solution(number):
    total = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

#Task 8

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

#Task 9

def are_you_playing_banjo(name):
    if name.lower().startswith("r"):
        return name + " plays banjo"
    return name + " does not play banjo"

#Task 10

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

#Task 11

def count_sheeps(sheep):
    return sheep.count(True)

#Task 12

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
