'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # If the length of the word is less than 2, return 0
    if len(word) < 2:
        return 0
    # If the current character is t, see if next one is h
    # Return this solution plus the solution for the string sliced
    if word[0] =='t' and word[1] =='h':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])

count_th("abcthefthghith")
