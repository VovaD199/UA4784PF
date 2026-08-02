def solution(number):
    if number < 0:
        return 0

    return sum(
        num
        for num in range(number)
        if num % 3 == 0 or num % 5 == 0
    )
