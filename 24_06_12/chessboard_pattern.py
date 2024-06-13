"""
Program to generate chessboard pattern
"""

if __name__ == '__main__':
    size = 5
    chessboard = ""

    for row in range(size):
        start_char = '0' if row % 2 == 0 else '1'
        for col in range(size):
            chessboard += start_char
            start_char = '1' if start_char == '0' else '0'
        chessboard += '\n'
    print(chessboard)
