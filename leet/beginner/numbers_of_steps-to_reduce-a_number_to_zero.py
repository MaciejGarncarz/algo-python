# 1342. Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def numberOfSteps(number: int) -> int:
    steps:int = 0
    while number > 0:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number - 1

        steps = steps + 1
    
    return steps


print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(123))



