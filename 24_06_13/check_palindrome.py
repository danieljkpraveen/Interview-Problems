"""
Check if string is palindrome without slicing
"""

def is_palindrome(input_str: str) -> bool:
    length = len(input_str)
    for index in range(length // 2):
        if input_str[index] != input_str[length - 1 -index]:
            return False
    return True


if __name__ == '__main__':
    input_str = "madm"
    result: bool = is_palindrome(input_str)
    if result:
        print("String is palindrome")
    else:
        print("String is not palindrome")
