# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List


def minCostClimbingStairsTopDown(cost: List[int]) -> int:
    memo = {}
    def climb(n: int):
        if n <= 1:
            return 0

        if n in memo:
            return memo[n]
        
        memo[n] = min(climb(n - 1) + cost[n - 1], climb(n - 2) + cost[n - 2])
        return memo[n]
   
    return climb(len(cost))

def minCostClimbingStairsBottomUp(cost: List[int]) -> int: 
    stairs = [0] * (len(cost) + 1)

    stairs[0] = 0
    stairs[1] = 0

    for index in range(2, len(stairs)):
        stairs[index] = min(stairs[index - 1] + cost[index - 1], stairs[index - 2] + cost[index - 2])
    
    return stairs[len(cost)]


cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairsTopDown(cost))
print(minCostClimbingStairsBottomUp(cost))


