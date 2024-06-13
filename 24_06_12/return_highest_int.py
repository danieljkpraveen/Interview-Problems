"""
Write a function that takes an unsigned integer 'n' as an argument which is a
natural number (ie, greater than zero), and returns an unsigned integer that 
is the highest number possible by rearranging the digits of integer 'n'.
Preceding zeros are not counted.

E.g. if number passed is 786, the retum value should be 876 which is the highest
integer possible by arranging digits 7,8 and 6.

"""

if __name__ == '__main__':
    number: int = input("Enter a number: ")
    if int(number) <= 0:
        print("Enter a positive number greater than 0")
        exit()
    else:
        digits = sorted(number, reverse=True)
        highest_number = int("".join(digits))
        print(highest_number)