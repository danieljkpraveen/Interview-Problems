"""
Rotate a list by k

Example: 
l = [1,2,3,4,5]
k = 3
output: [3,4,5,1,2]
"""

from typing import List


def rotate_list(numbers: List[int], k: int) -> List[int]:
    length: int = len(numbers)
    k: int = k % length
    """
    if k is greater than list, rotate by reminder of l%length
    if k=8 and length=5, 8%5=3. Rotating by 3 is the same as rotating by 8
    """
    return numbers[-k:] + numbers[:-k]
    """
    numbers[-k] refers to the element at index (len(numbers) - 3).
    Here, len(numbers) is 5, so -3 translates to (5 - 3) = 2.
    However, negative indices refer to elements in reverse order.
    So, numbers[-3] actually points to the third element from the end,
    which is 3 in this list.
    """


if __name__ == '__main__':
    numbers: List[int] = [1, 2, 3, 4, 5]
    k: int = 3
    result: List[int] = rotate_list(numbers, k)
    print(result)