"""
Count the occurance of each item in the list and pair them as tuples
"""

if __name__ == '__main__':
    input_list = [4, 6, 2, 4, 3, 4, 2, 2]
    count_dict = {}

    for element in input_list:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    result = list(count_dict.items())
    print(result)