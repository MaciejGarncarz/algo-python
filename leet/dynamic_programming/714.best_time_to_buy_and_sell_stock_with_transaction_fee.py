# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

from typing import Dict, List, Tuple


def maxProfit(prices: List[int], fee: int) -> int:
    memo: Dict[Tuple[int, bool], int] = {}
    def dp(day: int, holding: bool) -> int:
        if (day, holding) in memo:
            return memo[(day, holding)]

        if(day == len(prices)):
            return 0

        answer = dp(day + 1, holding)
        if holding:
            answer = max(answer, (prices[day] + dp(day + 1, False)) - fee)
        else:
            answer = max(answer, (-prices[day] + dp(day + 1, True)))

        memo[(day, holding)] = answer 
        return answer
    

    return dp(0, False)

prices = [1,3,2,8,4,9]
fee = 2
print(maxProfit(prices, fee))




