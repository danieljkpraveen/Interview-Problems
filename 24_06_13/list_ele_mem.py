"""
Check if list items are in the same memory location
"""

from typing import List


def check_memloc(inp_lst: List[int]) -> bool:
    return len(set(map(id, inp_lst))) == 1

if __name__ == '__main__':
    # inp_lst = [1, 2, 3, 4, 5]
    inp_lst = [1, 1, 1, 1]
    print(check_memloc(inp_lst))


"""
The function check_same_memory(l) takes a list l as input.

Inside the function, the map function is used to apply the id function to
each element in the list. The id function returns the memory address of an
object, so map(id, l) returns a list of memory addresses for the elements in l.

The set function is then used to convert this list of memory addresses into a set.
A set in Python is an unordered collection of unique elements, so any duplicate
memory addresses are removed.

Finally, len(set(map(id, l))) returns the number of unique memory addresses in the
list. If all elements in the list are stored at the same memory address, this will
be 1. Therefore, len(set(map(id, l))) == 1 checks if all elements in the list are
stored at the same memory address and returns True if they are and False otherwise.
"""