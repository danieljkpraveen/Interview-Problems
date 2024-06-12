"""
Program to check if number is armstrong number
"""

def check_armstrong(number: int) -> str:
    number_str: str = str(number)
    sum_of_powers = 0

    for digit in number_str:
        sum_of_powers += int(digit) ** len(number_str)

    if sum_of_powers == number:
        return f"{number} is an armstrong number"
    return f"{number} is not an armstrong number"


if __name__ == '__main__':
    number: int = 153
    result: str = check_armstrong(number)
    print(result)