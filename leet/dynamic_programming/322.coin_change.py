# https://leetcode.com/problems/coin-change/editorial/

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    memo = {}
    def dp(curr):
        if curr == 0:
            return 0
        if curr > 0:
            testa = dp(curr - coins[2]) + 1
            testb = dp(curr - coins[1]) + 1
            testc = dp(curr - coins[0]) + 1
            memo[curr] = min(testa, testb, testc) + 1
            return memo[curr]
        else:
            return 1
    
    return dp(amount)


print(coinChange([1,2,5], 11))
        
        


    