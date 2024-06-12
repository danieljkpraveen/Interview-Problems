"""
Given a list of strings, group them into lists of anagrams

Example:
i=["eat","tea","tan","ate","nat","bat"]
o/p:[["eat","tea","ate"],["tan","nat"],["bat"]]
"""

from typing import List
from collections import defaultdict


def group_anagrams(words: List[str]) -> List[str]:
    anagram_groups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    return list(anagram_groups.values())


if __name__ == '__main__':
    words: List[str] = [
        "eat",
        "tea",
        "tan",
        "ate",
        "nat",
        "bat",
    ]
    results: List[str] = group_anagrams(words)
    print(results)