# https://leetcode.com/problems/maximum-units-on-a-truck/description/

from typing import List


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    sortedBoxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    
    answer = 0
    for box in sortedBoxes:
        for _ in range(box[0]):
            if truckSize == 0:
                break
            
            answer += box[1]
            truckSize -= 1
    
    return answer



boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(maximumUnits(boxTypes, truckSize))