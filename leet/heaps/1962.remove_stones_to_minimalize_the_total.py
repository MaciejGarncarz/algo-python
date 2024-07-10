# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/

from heapq import *
from math import floor
from typing import List


def minStoneSum(piles: List[int], k: int) -> int:
    heap = []

    # can also initialize heap with heap = [-num for num in piles]

    for pile in piles:
        heappush(heap, -pile)
    
    for _ in range(k):
        pile = heappop(heap)
        reducedPile = floor(pile/2)
        heappush(heap,  reducedPile)
    
    answer = 0
    for x in heap:
        answer = answer + x
    
    return abs(answer)

piles = [4,3,6,7]
k = 3

print(minStoneSum(piles, k))

