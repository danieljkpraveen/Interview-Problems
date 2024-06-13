"""
Count the occurance of each character in the string
"""

if __name__ == '__main__':
    input_str: str = "i love india India"
    count = {}

    for character in input_str:
        if character == ' ':
            continue
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    print(count)
