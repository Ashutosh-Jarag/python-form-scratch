"""
String Challenge
Have the function stringChallenge (stz)
take the strparameter being passed and modify it using the following algorithm.
Replace every letter in the string with the letter following it in the alphabet (le. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
Examples
Input: "hello*3"
Output: Ifemp*3
Input: "fun times!"
Output: gv Ujnft!
Browse Resources
powered by Cogle
Docstring for string_Challenge.ch3
"""
def stringChallenge(stz):
    result = ""

    for ch in stz:
        # STEP 1: Shift letters
        if 'a' <= ch <= 'z':
            if ch == 'z':
                new_char = 'a'
            else:
                new_char = chr(ord(ch) + 1)

        elif 'A' <= ch <= 'Z':
            if ch == 'Z':
                new_char = 'A'
            else:
                new_char = chr(ord(ch) + 1)

        else:
            # Non-letter characters remain unchanged
            result += ch
            continue

        # STEP 2: Capitalize vowels
        if new_char.lower() in 'aeiou':
            new_char = new_char.upper()

        result += new_char

    return result


# Test cases
print(stringChallenge("hello*3"))     # Ifmmp*3
print(stringChallenge("fun times!"))  # gv Ujnft!
