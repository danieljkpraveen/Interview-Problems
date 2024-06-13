"""
Find which character occurs most number of times
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
    max_char = max(count, key=count.get)
    max_count = count[max_char]
    print(f"{max_char} occurs {max_count} times")
