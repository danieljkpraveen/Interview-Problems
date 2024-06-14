"""
Program that computes the maximum area of water that
can be contained between the vertical lines
"""

def max_area(height):
    maxarea = 0
    left = 0
    right = len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        maxarea = max(maxarea, h * w)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxarea


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(height))
