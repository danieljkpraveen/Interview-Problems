"""
Program to print all prime numbers in an interval
"""

def check_prime(number: int) -> bool:
    if number <= 1:
        return False

    elif number <= 3:
        return True

    elif number%2 == 0 or number%3 == 0:
        return False

    i: int = 5
    while i *i <= number:
        if (number % i == 0 \
            or number % (i+2) == 0):
            return False
        i+=6
    return True


def find_primes(start: int, end: int) -> str:
    primes = []
    for num in range(start, end+1):
        if check_prime(num):
            primes.append(num)

    return f'Prime numbers from {start} - {end}:\n{primes}'


if __name__ == '__main__':
    start: int = int(input("Enter start: "))
    end: int = int(input("Enter end: "))
    result: str = find_primes(start, end)
    print(result)

