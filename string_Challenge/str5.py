"""
Count vowels and consonants in a string (using loops only)
Docstring for string_Challenge.str5
"""

def count(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    c_count = 0
    v_count = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            elif ch in consonants:
                c_count += 1
    return v_count, c_count

v, c = count("hello world")
print(c)
print(v)