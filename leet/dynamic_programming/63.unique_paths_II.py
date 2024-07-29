# https://leetcode.com/problems/unique-paths-ii/description/

from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    memo = {}
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    def move(row, col):
        if (row, col) in memo:
            return memo[(row, col)]
        
        if obstacleGrid[row][col] == 1:
            return 0
        
        if row == 0 and col == 0:
            return 1
        
        ways = 0
        if row > 0:
            ways += move(row - 1, col)
        if col > 0:
            ways += move(row, col - 1)
        
        memo[(row, col)] = ways
        return ways

    return move(m -1, n -1)
    


print(uniquePathsWithObstacles([[1]]))

        

        
