import math
import task2
import task3


# -------------------
# Task2
# -------------------

password_tests = [
    ("Test@123", True),
    ("test@123", False),
    ("TEST@123", False),
    ("Test123", False),
]

for password, expected in password_tests:
    result = task2.password_check(password)
    print(f"{password} expected={expected} got={result}")


# -------------------
# Task3
# -------------------

math_tests = [
    ("Rectangle", task3.rectangle_area(5, 4), 20),
    ("Triangle", task3.triangle_area(10, 4), 20),
    ("Circle", task3.circle_area(2), 4 * math.pi),
]

for name, result, expected in math_tests:
    ok = math.isclose(result, expected)
    print(f"{name} expected={expected} got={result} -> {ok}")