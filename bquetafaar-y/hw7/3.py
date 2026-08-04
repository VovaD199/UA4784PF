phrase = input()

def characters(phrase):
    '''Characters counting function'''
    result = {}
    for i in phrase:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

print(characters(phrase))