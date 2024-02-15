# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4610/

input =  "/hello../world"
# "/a/./" -> /a - V
# "/a/.." -> / - V
# "/a/./b" -> /a/b - V
# "/a/./b/.." -> /a
# "/..." -> /... - V
# "/.../" -> /... - V
# "/." -> /  - V
# "/../" -> /


# Maybe the easier approach is to iterate through stack
# Basically create fragments of path between '/{}/
# If something is wrong we can just pop until stack is again correct
def simplifyPath(path: str) -> str:
    stack = []
    stack.append('/')

    # Always start with '/'
    # If there are two '/' next to each other leave only one
    # If there is './' pop unitl we meet '/'
    # If there is '../ pop until we meet second '/'
    # If there is '.../ this is valid directory
    # At the end truncate until there is valid char


    for char in path:
        # Get last character in stack
        lastCharacter = stack[-1]
        if char is '/':
            if lastCharacter is '/':
                pass
            elif lastCharacter is '.':
                tempStack = []
                while len(stack) > 1 and stack[-1] is not '/':
                    poppedCharacter = stack.pop()
                    tempStack.append(poppedCharacter)
                partOfPath = "".join(tempStack)
                if partOfPath == ".":
                    if len(stack) > 1:
                        pass
                elif partOfPath == "..":
                    if len(stack) > 1:
                        stack.pop()
                    while len(stack) > 1 and stack[-1] is not '/':
                        stack.pop()
                else:
                    while tempStack:
                        stack.append(tempStack.pop())
                    stack.append(char)
            else:
                stack.append(char)
        else:
            stack.append(char)

    if len(stack) > 1 and stack[-1] == '/':
        stack.pop()

    tempStack = []
    while len(stack) > 1 and stack[-1] is not '/':
        poppedCharacter = stack.pop()
        tempStack.append(poppedCharacter)
    partOfPath = "".join(tempStack)
    if partOfPath == ".":
        if len(stack) > 1:
            stack.pop()
    elif partOfPath == "..":
        stack.pop()
        while len(stack) > 1 and stack[-1] is not '/':
            stack.pop()
    else:
         while tempStack:
            stack.append(tempStack.pop())

    if len(stack) > 1 and stack[-1] == '/':
        stack.pop()

    return "".join(stack)

print(simplifyPath(input))