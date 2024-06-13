"""
Sort list of integers in ascending order
"""

from typing import List


def sort_int_asc(numbers: List[int]) -> List[int]:
    numbers_len: int = len(numbers)
    for i in range(numbers_len):
        min_idx = i
        for j in range(i + 1, numbers_len):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


def sort_int_desc(numbers: List[int]) -> List[int]:
    numbers_len: int = len(numbers)
    for i in range(numbers_len):
        max_idx = i
        for j in range(i + 1, numbers_len):
            if numbers[j] > numbers[max_idx]:
                max_idx = j
        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
    return numbers


if __name__ == '__main__':
    numbers_1: List[int] = [45, 72, 82, 99, 2, 77, 8]
    numbers_2: List[int] = [45, 72, 82, 99, 2, 77, 8]
    asc_result: List[int] = sort_int_asc(numbers_1)
    desc_result: List[int] = sort_int_desc(numbers_2)
    print(asc_result)
    print(desc_result)
