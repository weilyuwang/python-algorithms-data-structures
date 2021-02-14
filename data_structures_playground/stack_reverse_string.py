"""
Use a stack data structure to reverse a string

Example: 
"Hello" -> "olleH"

"""
from stack import Stack


def reverse_string(input_str):
    # Loop through the string and push character by character onto stack
    stack = Stack()

    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


input_str = "Hello"
print(reverse_string(input_str))
