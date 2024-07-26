# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

from typing import Dict, List, Tuple


def maxProfit(prices: List[int]) -> int:
    memo: Dict[Tuple[int, bool, bool], int] = {}

    def dp(day: int, holding: bool, cooldown: bool) -> int:
        if (day, holding, cooldown) in memo:
            return memo[(day, holding, cooldown)]

        if(day >= len(prices)):
            return 0
        
        answer = dp(day + 1, holding, cooldown)

        if holding:
            answer = max(answer, prices[day] + dp(day + 2, False, True))
        else:
            answer = max(answer, (-prices[day] + dp(day + 1, True, False)))


        memo[(day, holding, cooldown)] = answer 
        return answer
    

    return dp(0, False, False)


print(maxProfit(prices = [1,2,3,0,2]))