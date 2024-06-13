"""
Program to check if a string containing brackets is balanced (all brackets are closed)
"""

def check_valid_brackets(input_string: str) -> bool:
    stack = []
    bracket_map = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for character in input_string:
        if character in bracket_map.values(): # if character is open bracket
            stack.append(character)
        elif character in bracket_map: # if character is close bracket
            if not stack or stack.pop() != bracket_map[character]: # check if close bracket is at top of stack
                return False
    return True


if __name__ == '__main__':
    input_string: str = "{{[{((()))}]}}"
    result: bool = check_valid_brackets(input_string)
    if result:
        print("valid bracket string")
    else:
        print("invalid bracket string")
