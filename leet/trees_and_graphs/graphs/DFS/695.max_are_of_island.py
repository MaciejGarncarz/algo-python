# https://leetcode.com/problems/max-area-of-island/description/

from typing import List


def maxAreaOfIsland(grid: List[List[str]]) -> int:
    answer = 0
    currentMax = []

    def valid(row, col):
        return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
    def dfs(row, col):
        for dx, dy in directions:
            next_row, next_col = row + dy, col + dx
            if valid(next_row, next_col) and (next_row, next_col) not in seen:
                currentMax.append(0)
                seen.add((next_row, next_col))
                dfs(next_row, next_col)
        
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seen = set()
    m = len(grid)
    n = len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1 and (row, col) not in seen:
                seen.add((row, col))
                dfs(row, col)
                answer = max(answer, len(currentMax) + 1)
                currentMax = []
        
    return answer
    

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))