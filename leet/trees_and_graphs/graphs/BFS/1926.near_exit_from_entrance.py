# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

from collections import deque
from typing import List


def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    width = len(maze[0])
    height = len(maze)


    def valid(row, col):
        return 0 <= row < height and 0 <= col < width and maze[row][col] == "."
    
    seen = {(entrance[0], entrance[1])}
    queue = deque([(entrance[0], entrance[1], 0)])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    up = (-1, 0)


    while queue:
        row, col, steps = queue.popleft()

        for dx, dy in directions:
            nextRow, nextCol = row + dx, col + dy
            if valid(nextRow, nextCol) and (nextRow, nextCol) not in seen:
                seen.add((nextRow, nextCol))
                queue.append((nextRow, nextCol, steps + 1))
            elif (nextRow >= height or nextCol >= width or nextRow == -1 or nextCol == -1) and (row != entrance[0] or col != entrance[1]):
                return steps

    return -1




maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

print(nearestExit(maze, entrance))