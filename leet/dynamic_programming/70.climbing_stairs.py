# https://leetcode.com/problems/climbing-stairs/description/


def climbStairsTopDown(n: int) -> int:
    memo = {}

    def climb(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        testa = climb(n - 1)
        testb = climb(n - 2)
        memo[n] =  testa +testb
        return memo[n]
    
    return climb(n)


def climbStairsBottomUp(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for x in range(3, n + 1):
        dp[x] = dp[x - 1] + dp[x - 2]
    
    return dp[n]
     
        

print(climbStairsTopDown(3))
print(climbStairsBottomUp(3))