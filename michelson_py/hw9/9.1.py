from random import randint

number = randint(1, 100)

for attempt in range(1, 11):
    guess = int(input(f"Спроба {attempt}/10. Введіть число: "))

    if guess == number:
        print("Вітаю! Ви вгадали число!")
        break
    elif guess < number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")

else:
    print(f"Ви використали всі 10 спроб. Загадане число було: {number}")