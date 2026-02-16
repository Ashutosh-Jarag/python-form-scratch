"""
Question.-String Challenge
Have the function stringChallenge (sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: Love
"""

def stringChallenge(sen):
    cleaned = ""

    for ch in sen:
        if ch.isalpha() or ch == " ":
            cleaned += ch 
        else: 
            cleaned += " "

    
    
    words = []
    word = ""

    for ch in cleaned: 
        if ch != " ":
            word += ch
        else:
            if word != "":
                words.append(word)
                word = ""
    if word != "":
        words.append(word)

    
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
            
    return longest

print(stringChallenge("fun&!! time"))         # time
print(stringChallenge("I love dogs"))         # love
print(stringChallenge("Hello world123 567"))  # world123