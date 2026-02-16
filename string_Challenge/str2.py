"""
Have the function stringChallenge (stz) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna diroW olleH.
Examples
Input: "coderbyte"
Output: etybredoc
Input: "I Love Code"
Output: edoC evol I
Browse Resources
powered by Google
Search for any documentation you might need for this problem. For example: array indexing, React props, etc.
"""
def string(input):
    store = ""

    for i in range(len(input)-1,-1,-1):
        store += input[i]

    return store


print(string("coderbyte"))      # etybredoc
print(string("I Love Code"))    # edoC evol I)
