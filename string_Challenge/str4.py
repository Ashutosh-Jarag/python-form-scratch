"""
Reverse a string without using slicing ([::-1])

Docstring for string_Challenge.str4
"""

def reverse(s):
    result = ""
    for ch in s:
        result = ch + result

    return result
print(reverse("abcd"))
