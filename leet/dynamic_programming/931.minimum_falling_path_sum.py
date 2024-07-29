# https://leetcode.com/problems/minimum-falling-path-sum/description/

from typing import List


# Mozna by sie tutaj tez zastanowic zeby:
def minFallingPathSum(matrix: List[List[int]]) -> int:
    memo = {}
    n = len(matrix)
    result = float("inf")

    def move(row, col) -> int:
        if (row, col) in memo:
            return memo[row, col]

        if row >= n or col >= n or col < 0: # nie sprawdzac tego wogole
            return 0

        currentValue = matrix[row][col]
        answer = currentValue
        curr = float("inf")
        
        # za to w miejscach zaznaczonych nie pozwolic nigdy aby wyszlo poza granice matrycy
        if row < n:  # mark
            curr = min(curr, move(row + 1, col))
        if col < n and col > 0: # mark
            curr = min(curr, move(row + 1, col - 1))
        if row < n and col < n-1: # mark
            curr = min(curr, move(row + 1, col + 1))
        
        answer += curr
        memo[(row, col)] = answer
        return answer
    
    for x in range(0, n):
        result = min(result, move(0, x))
    return result


print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))



        



