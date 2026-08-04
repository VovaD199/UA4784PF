"""
Task 1.
Jenny has written a function that returns a greeting for a user. 
However, she's in love with Johnny, and would like to greet him slightly different. 
She added a special case to her function, but she made a mistake.
"""
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, " + name + "!"


"""
Task 2.
Simple: Find The Distance Between Two Points.
Given two ordered pairs calculate the distance between them. Round to two decimal places.
This should be easy to do in 0(1) timing.
"""
def distance(point1, point2):
    import math

    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)

""""
Task 3.
No yelling!
Write a function taking in a string like 
WOW this is REALLY          amazing and returning Wow this is really amazing. 
String should be capitalized and properly spaced.

Ex.
"HELLO CAN YOU HEAR ME" --> "Hello can you hear me"
"now THIS is REALLY interesting" --> "Now this is really interesting"
"THAT was EXTRAORDINARY!" --> "That was extraordinary!"
"""
def format_string(input_string):
    formatted_string = ' '.join(input_string.split()).lower().capitalize()
    return formatted_string

"""
Task 4.
Convert a Number to a String!

DESCRIPTION:
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):

123  --> "123"
999  --> "999"
-100 --> "-100"
"""
def number_to_string(num):
    return str(num)

"""
Task 5.
Reversing Words in a String.

DESCRIPTION:

You need to write a function that reverses the words in a given string. Words are always separated by a single space.

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
"""
def reverse_words(input_string):
    words = input_string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

"""
Task 6.
Reverse List Order.

DESCRIPTION:

In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples (Input -> Output)

* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]
"""
def reverse_list(input_list):
    input_list.reverse()
    return input_list

"""
Task 7.
Multiples of 3 or 5.

DESCRIPTION:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If a number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)
"""
def solution(number):
    if number < 0:
        return 0

    multiples_sum = sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
    return multiples_sum

"""
Task 8.
Will you make it?

DESCRIPTION:
You were camping with your friends far away from home, 
but when it's time to go back, 
you realize that your fuel is running out and the nearest pump is 50 miles away! 
You know that on average, your car runs on about 25 miles per gallon. 
There are 2 gallons left.

Considering these factors, write a function that tells you 
if it is possible to get to the pump or not.

Function should return true if it is possible and false if not.
"""
def will_make_it(fuel, distance_to_pump, miles_per_gallon):
    max_distance = fuel * miles_per_gallon
    return max_distance >= distance_to_pump

"""
Task 9.
Are You Playing Banjo?

DESCRIPTION:
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
"""
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

"""
Task 10.
Convert boolean values to strings 'Yes' or 'No'.

DESCRIPTION:
Complete the method that takes a boolean value and return a "Yes" string for true, 
or a "No" string for false.
"""
def bool_to_word(value):
    return "Yes" if value else "No"

"""
Task 11.
Counting sheep...

DESCRIPTION:
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present 
in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
"""
def count_sheep(sheep_list):
    return sum(1 for sheep in sheep_list if sheep is True)

"""
Task 12.
Is this my tail?

DESCRIPTION:
Some new animals have arrived at the zoo. 
The zoo keeper is concerned that perhaps the animals do not have the right tails. 
To help her, you must correct the broken function to make sure that the second argument 
(tail), is the same as the last letter of the first argument 
(body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be non empty strings, and normal letters.
"""
def correct_tail(body, tail):
    return body[-1] == tail