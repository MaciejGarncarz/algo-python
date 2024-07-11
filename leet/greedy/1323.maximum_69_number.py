# https://leetcode.com/problems/maximum-69-number/description/

def maximum69Number (num: int) -> int:
    numList = list(str(num))

    for i in range(len(numList)):
        number = numList[i]
        if number is '6':
            numList[i] = '9'
            break
    
    return int(''.join(numList))


num = 9999

print(maximum69Number(num))