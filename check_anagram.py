"""
check if two strings are anagram of each other
"""

def check_anagram(subject: str, anagram: str) -> bool:
    """
    subject is the original word
    anagram is the letters rearranged new word
    """

    char_count = {}

    if len(subject) != len(anagram):
        return False
    for character in subject:
        char_count[character] = char_count.get(character, 0) + 1
        # get (char:idx) from char_count, set idx = 0 if char not already in char_count
    for character in anagram:
        if (character not in char_count
            or char_count[character] == 0):
            return False
        char_count[character] -= 1
    return True


if __name__ == '__main__':
    subject: str = input("Enter subject: ")
    anagram: str = input("Enter anagram: ")
    result: bool = check_anagram(subject, anagram)
    if result:
        print("This is an anagram")
    else:
        print("This is not an anagram")