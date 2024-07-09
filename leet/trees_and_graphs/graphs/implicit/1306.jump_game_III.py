# https://leetcode.com/problems/jump-game-iii/description/ 

from collections import defaultdict, deque
from typing import List, Tuple


def canReach(arr: List[int], start: int) -> bool:
    def valid(index: int) -> bool:
        return index <= len(arr) - 1 and index >= 0

    def nextMove(index: int) -> List[int]:
        moves = []
        if not valid(index):
            return moves
        
        moves.append(index + arr[index])
        moves.append(index - arr[index])

        return moves
    
    queue = deque([start])
    seen = set()
    seen.add(start)

    while queue:
        index = queue.popleft()

        if arr[index] == 0:
            return True
        
        for move in nextMove(index):
            if move not in seen and valid(move):
                queue.append(move)
                seen.add(move)
        
    return False





# arr = [4,2,3,0,3,1,2]
# start = 5

arr = [4,2,3,0,3,1,2] 
start = 0

# arr = [3,0,2,1,2] 
# start = 2

print(canReach(arr, start))