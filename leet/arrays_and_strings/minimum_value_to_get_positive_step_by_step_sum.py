from typing import List


input = [1, 2]
# [-3, -1, -4, 0, 2]

def Test():
    arr = [1, 2, 3]
    for i in arr:
        print(i)

    for i in arr:
        print(i)

    


# this was also good although time complexity is worse
def findMinimumPositiveStepbyStepSumValue(nums: List[int]) -> int:
    prefix = [nums[0]]
    minimumPositiveValue = 1
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    for i in range(len(prefix)):
        difference = minimumPositiveValue + prefix[i]
        if difference <= 0:
            minimumPositiveValue = (prefix[i] * -1) + 1
            difference = 0

    return minimumPositiveValue

#leet code aproach
def minStartValue(nums: List[int]) -> int:
        # We use "total" for current step-by-step total, "min_val" for minimum 
        # step-by-step total among all sums. Since we always start with 
        # startValue = 0, therefore the initial current step-by-step total is 0, 
        # thus we set "total" and "min_val" be 0. 
    min_val = 0
    total = 0

        # Iterate over the array and get the minimum step-by-step total.
    for num in nums:
        total += num
        min_val = min(min_val, total)

        # We have to change the minimum step-by-step total to 1, 
        # by increasing the startValue from 0 to -min_val + 1, 
        # which is just the minimum startValue we want.
    return -min_val + 1


print(minStartValue(input))