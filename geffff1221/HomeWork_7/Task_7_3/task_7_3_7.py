def solution(number):
    summa = 0
    for i in range(0, number):
        if i % 3 == 0 and i % 5 == 0:
            summa += i
        elif i % 3 == 0 or i % 5 == 0:
            summa += i
        elif number < 0:
            summa = 0
    return summa