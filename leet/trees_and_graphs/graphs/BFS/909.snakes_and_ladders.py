# https://leetcode.com/problems/snakes-and-ladders/description/


from collections import deque
from typing import List, Tuple


def snakesAndLadders(board: List[List[int]]) -> int:
    NORMAL_TILE = -1
    maxTile = len(board) ** 2

    numeredBoard: List[Tuple[int, int]] = [0] * (maxTile + 1)
    label = 1
    revert: bool = False
    for row in range(len(board) - 1, -1, -1):
        tiles = board[row]
        if revert:
            tiles.reverse()
        
        for tile in tiles:
            numeredBoard[label] = tile
            label = label + 1
            
        revert = not revert


    queue = deque(([(1, 0)]))
    visited = set()

    while queue:
        current, totalDiceRolls = queue.popleft()

        if current == maxTile:
            return totalDiceRolls
        
        for roll in range(current + 1, min(current + 6, maxTile) + 1):
            next = roll
            destination = numeredBoard[next]
            if destination != NORMAL_TILE:
                next = destination

            if next not in visited:
                visited.add(next)
                queue.append((next, totalDiceRolls + 1))

    return -1

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
board2 = [[-1,-1,-1],[-1,9,8],[-1,8,9]]
board3 = [[-1,-1],[-1,3]]
board4 = [[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]
board5 = [[-1,-1,-1,9,-1,-1],[-1,-1,10,7,-1,-1],[-1,-1,-1,-1,-1,20],[-1,14,-1,-1,15,20],[31,29,-1,-1,7,36],[-1,-1,-1,13,18,5]]


# print(snakesAndLadders(board))
# print(snakesAndLadders(board2))
# print(snakesAndLadders(board3))
# print(snakesAndLadders(board4))
print(snakesAndLadders(board5))

