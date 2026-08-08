import math

def jenny_secret_message(name):
    """Return a greeting for the given name"""
    
    if name == "Johnny":
        return "Hello, my love!"
    
    return f"Hello, {name}!"

def distance_between_two_pairs(point1, point2):
    """Calculates distance between two points"""
    
    distance = math.sqrt(((point1[0] - point2[0])**2) + ((point1[1] - point2[1])**2))
    
    return round(distance, 2)

def no_yelling(text):
    """Formats text with proper spacing and capitalization"""
    words = text.split()
    new_text = " ".join(words)
    result = new_text.capitalize()
    
    return result
    
def number_to_string(number):
    """Transform a number into a string"""
    
    result = str(number)
    
    return result
    
def reversing_words(text):
    """Reverses the words in a given string"""
    
    new_text = text.split()
    new_text = new_text[::-1]
    result = " ".join(new_text)
    
    return result

def reverse_list_order(list_x):
    """Returns a list with the reverse order"""
    
    result = list_x[::-1]
    
    return result

def multiples_of_3_or_5(number):
    """Returns the sum of all the multiples of 3 or 5 below a number"""
    
    if number < 0:
        return 0
    
    result = 0
    
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    
    return result

def fuel_level(distance, fuel_left, miles_per_gallon):
    """Tells if it is possible to get to the pump or not"""
   
    return fuel_left * miles_per_gallon >= distance

def are_you_playing_banjo(name):
    """Answers the question "Are you playing banjo?"""
    
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
def bool_to_word(boolean):
    """Convert boolean values to strings 'Yes' or 'No'"""
    
    if boolean:
        return "Yes"
    else:
        return "No"

def count_sheeps(sheep):
    """Counts the number of sheep present in the list"""
    
    count = 0
    
    for i in sheep:
        if i is True:
            count += 1
    
    return count

def correct_tail(body, tail):
    """Checks if the tail matches the last letter of the body"""
    if body[-1] == tail:
        return True
    else:
        return False

