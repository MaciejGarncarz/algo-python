# https://leetcode.com/problems/removing-stars-from-a-string/description/

input = "erase*****"

def remove_stars(s: str) -> str:
    stack = []
    deleteCharacter = '*'
    for _, x in enumerate(s):
        if x is deleteCharacter:
            stack.pop()
        else:
            stack.append(x)
    
    return "".join(stack)



print(remove_stars(input))