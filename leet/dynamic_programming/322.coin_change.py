# https://leetcode.com/problems/coin-change/editorial/

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    memo = {}

    def dp(curr):
        if curr in memo:
            return memo[curr]
        if curr == 0:
            return 0
        if curr < 0:
            return float('-inf')
        
        steps = float('inf')

        for x in coins:
            currSteps = dp(curr - x) + 1

            if currSteps > 0:
                steps = min(steps, currSteps)
        
        memo[curr] = steps
        return steps

    result = dp(amount)
    if result == float('inf'):
        return -1 
    return result


print(coinChange([1,2,5], 11))
        
        


    