# https://leetcode.com/problems/isomorphic-strings/description/

input1 = "egg"
input2 = "add"

# litery musza byc w tym samym miejscu

def is_isomporhic(s:str, t:str) -> bool:
    sMap = {}
    tMap = {}

    for index, x in enumerate(s):
        if x in sMap:
            sMap[x].append(index)
        else:
            sMap[x] = [index]

    for index, x in enumerate(t):
        if x in tMap:
            tMap[x].append(index)
        else:
            tMap[x] = [index]

    sKeys = list(sMap.keys())
    tKeys = list(tMap.keys())
    for x in range(0, len(sMap)):
        if sMap[sKeys[x]] != tMap[tKeys[x]]:
            return False
    
    return True


print(is_isomporhic(input1, input2))