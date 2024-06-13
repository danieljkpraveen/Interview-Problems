"""
Convert a string to list items
l="i am python welcome" output=["I"," Am"," Python"." Welcome"]
"""

if __name__ == '__main__':
    input_str: str = "I am python welcome"
    result = [word.capitalize() for word in input_str.split()]
    print(result)
