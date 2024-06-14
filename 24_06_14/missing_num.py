"""
Program that takes a list of unique integers nums containing numbers from 0 to n
but with one missing number, and returns the missing number.
Sample Input:nums = [3, 0, 1]
Expected Output:2
"""

from typing import List


def find_num(numbers: List[int]) -> int:
    length: int = len(numbers)
    total_sum = length * (length + 1) // 2
    actual_sum = sum(numbers)
    missing_number = total_sum - actual_sum
    return missing_number


if __name__ == '__main__':
    inp_numbers: List[int] = [3, 0, 1]
    result: int = find_num(numbers=inp_numbers)
    print(f"Missing number is {result}")
