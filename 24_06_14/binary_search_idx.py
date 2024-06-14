"""
Perform binary search and return the index of search element
if found, -1 if not found
"""

from typing import List


def binary_search(inp_lst: List[int], target: int) -> int:
    left, right = 0, len(inp_lst) - 1
    ##
    while left <= right:
        mid = (left+right) // 2
        if inp_lst[mid] == target:
            return mid
        elif inp_lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7]
    search: int = 5
    result: int = binary_search(inp_lst=numbers, target=search)
    print(f"{search} is at index {result}")
