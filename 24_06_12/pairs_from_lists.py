"""
program to create pairs from indexes between lists
"""

from typing import List

if __name__ == '__main__':
    a: List[int] = [1, 2, 3, 4, 5]
    b: List[int] = [11, 12, 13, 14, 15]

    output = []
    for index in range(len(a)):
        output.append((a[index], b[index]))

    print(output)
