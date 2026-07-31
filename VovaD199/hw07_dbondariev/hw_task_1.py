def get_largest_number(a, b):
    """Return the largest number of two numbers."""
    if a > b:
        return a
    return b

print(get_largest_number.__doc__)
print(get_largest_number(10, 25))


def get_largest_number(a, b):
    """Return the largest number of two numbers using max."""
    return max(a, b)

print(get_largest_number.__doc__)
print(get_largest_number(10, 25))


