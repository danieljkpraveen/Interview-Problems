"""
Write a Python function that rotates a given n x n 2D matrix matrix by 90 degrees clockwise.
Sample Input:matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Expected Output:[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]

"""

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
    return matrix


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(rotate_matrix(matrix))
