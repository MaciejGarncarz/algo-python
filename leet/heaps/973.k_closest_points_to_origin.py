# https://leetcode.com/problems/k-closest-points-to-origin/description/

from heapq import heappop, heappush
from math import sqrt
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    answer = []
    
    for cordinates in points:
        x = cordinates[0]
        y = cordinates[1]

        distance = (x + 0) ** 2 + (y + 0) ** 2
        distance = sqrt(distance)

        heappush(heap, (distance, [x, y]))

    for _ in range(k):
        _, cordinates = heappop(heap)
        answer.append(cordinates)

    return answer



points = [[3,3],[5,-1],[-2,4]]
k = 2

print(kClosest(points, k))