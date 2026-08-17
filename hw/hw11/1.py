def odd_even_number(n:int) -> str:
    if n<0:
        raise ValueError("The value should be non-negative!")
    return "odd" if n%2 else "even"

if __name__ == "__main__":
    age = 42
    try:
        age = int(input("Enter your age you see if it is odd or even:\n"))
        print("Your age is",odd_even_number(age))
    except ValueError as e:
        print(f"Error occured: {e}")

