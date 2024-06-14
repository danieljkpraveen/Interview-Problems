"""
Program that returns the total number of continuous
subarrays whose cumulative sum equals to k
"""

def subarray_sum(nums, k):
    count = 0
    sums = {0: 1}
    cum_sum = 0
    for num in nums:
        cum_sum += num
        if (cum_sum - k) in sums:
            count += sums[cum_sum - k]
        if cum_sum in sums:
            sums[cum_sum] += 1
        else:
            sums[cum_sum] = 1
    return count


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    print(subarray_sum(nums, k))
