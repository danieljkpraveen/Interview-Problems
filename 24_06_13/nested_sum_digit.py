"""
Get sum of digits and sum of the result

a = 12345
s1 = 1+2+3+4+5 (s1=15)
s2 = 1+5 (s2=6)
output = 6
"""

if __name__ == '__main__':
    number: int = 12345
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    print(number)
