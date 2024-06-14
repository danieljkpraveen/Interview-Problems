"""
Find a peak element in a given list. A peak element is an element
that is greater than its neighbors.
"""

def find_peak_element(nums):
    if not nums:
        return None
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return nums[left]



if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(find_peak_element(nums))
