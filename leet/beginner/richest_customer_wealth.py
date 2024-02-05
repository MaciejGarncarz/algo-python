#1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

accounts1 = [[1,2,3], [3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]

def maximumWealth(accounts: list[list[int]]) -> int:
    result = 0
    for x in accounts:
        tempSum = sum(x)
        if result < tempSum:
            result = tempSum

    return result

# Max solution 
# def maximumWealth(self, accounts: List[List[int]]) -> int:
#     return max([sum(acc) for acc in accounts])


print(maximumWealth(accounts3))