# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/


from typing import List
from heapq import *


def connectSticks(sticks: List[int]) -> int:
    heap = []
    costs = [0]

    for stick in sticks:
        heappush(heap, stick)
    
    while len(heap) > 1:
        firstStick = heappop(heap)
        secondStick = heappop(heap)

        connectedStick = firstStick + secondStick

        costs.append(connectedStick)

        heappush(heap, connectedStick)
    
    return sum(costs)


sticks = [1175,8967,1382,8748,8612,7067,5979,8237,9691,389,5801,7387,8620,6674,1610,7444,6969,970,9463,7727,5044,1834,3426,3192,9473,2300,3647,6492,3166,3486,454,6077,670,4929,1266,8288,8554,8432,4724,8553,2442,1776,2704,1276,2933,3376,8259,8548,1563,3884]

#1363767 1397754
print(connectSticks(sticks))
