NUMBER_TO_DAY = {
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
}

def number_to_day(n:int) -> str:
    if n<=0 or n>=8:
        raise ValueError(r"The value 'n' should be [1, 7], n\in\mathbb{N} (yes, TEX code in python)")
    return NUMBER_TO_DAY[n]


if __name__ == "__main__":
    try:
        n = int(input("Enter day number (from 1 to 7 included): "))
        print(f"THIS IS {number_to_day(n)} (insert shocked face)")
    except ValueError as e:
        e = str(e)
        print(f"Error occured: {e}")
