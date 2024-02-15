# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4611/

input = ""

# aa - V
# aA - X
# Aa - X

def makeGood(s: str) -> str:
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            lastCharacterInStack = stack[-1]
            temp = char
            if temp.islower():
                temp = temp.upper()
            else:
                temp = temp.lower()

            if lastCharacterInStack == temp:
                stack.pop()
            else:
                stack.append(char)

    return "".join(stack)


print(makeGood(input))