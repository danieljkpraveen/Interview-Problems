"""
find the longest common prefix at the beginning of string amongst an array of strings.
If there is no common prefix, return an empty string

Example 1: Input: strs = ["flower", "flow", "flight"] Output: "fl"
Example 2: Input: strs = ["dog", "racecar", "car"]Output: ""

Explanation: There is no common prefix among the input strings.
"""

from typing import List


def find_longest_prefix(strings: List[str]) -> str:
    shortest_string = min(strings, key=len) # find length of each item in list to find smallest string
    for index, character in enumerate(shortest_string):
        for item in strings:
            if item[index] != character:
                return shortest_string[:index]
    return shortest_string


if __name__ == '__main__':
    strings: List[str] = [
        "flower",
        "flow",
        "flight",
        "fly",
    ]
    result: str = find_longest_prefix(strings)
    print(result)
