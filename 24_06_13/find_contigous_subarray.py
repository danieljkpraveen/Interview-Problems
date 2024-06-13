"""
Program to find the maximum sum of contigous subarray in an array of int
"""

from typing import List


def max_subarray_sum(numbers: List[int]) -> int:
    max_current = max_global = numbers[0]
    for index in range(1, len(numbers)):
        max_current = max(numbers[index], max_current + numbers[index])
        if max_current > max_global:
            max_global = max_current
    return max_global


if __name__ == '__main__':
    numbers: List[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result: int = max_subarray_sum(numbers)
    print(result)