# https://leetcode.com/problems/destination-city/description/

from typing import List


input = [["B","C"],["D","B"],["C","A"]]

def destination_city(paths: List[List[str]]) -> str:
    hashMap = {}

    for x in range(0, len(paths)):
        cities = paths[x]
        sourceCity = cities[0]
        destinationCity = cities[1]

        hashMap[sourceCity] = 1
        
        if destinationCity in hashMap:
            hashMap[destinationCity] = 1
        else:
            hashMap[destinationCity] = 0

    for key, value in hashMap.items():
        if value == 0:
            return key


print(destination_city(input))
            