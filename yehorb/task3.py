def count(string):
    result = {}

    for i in string:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result


string = input("Enter a string: ")

print(count(string))