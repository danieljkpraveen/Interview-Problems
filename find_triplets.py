'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and 
nums[i] + nums[j] + nums[k] == 0.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

from typing import List


def find_triplets(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for index, num in enumerate(nums[:-2]):
        if index > 0 and nums[index] == nums[index-1]:
            continue
        left, right = index+1, len(nums)-1
        while left < right:
            sum = num + nums[left] + nums[right]
            if sum < 0:
                left+=1
            elif sum > 0:
                right-=1
            else:
                result.append((num, nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left+=1
                while left < right and nums[right] == nums[right-1]:
                    right-=1
                left+=1; right-=1
    return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    triplets: List[List[int]] = find_triplets(nums)
    print(f"The triplets for array : {nums} is\n{triplets}")
