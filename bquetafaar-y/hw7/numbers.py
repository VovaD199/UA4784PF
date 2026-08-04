number = int(input())

def solution(number):
    summ = 0
    if number < 0:
        return 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    return summ
print(solution(number))
  