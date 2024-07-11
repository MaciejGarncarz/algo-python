#https://leetcode.com/problems/reduce-array-size-to-the-half/description/

from collections import defaultdict
from math import floor
from typing import List


def reduceArray(arr: List[int]) -> int:
    hashSet = defaultdict()
    selected = set()
    removed_count = 0

    for num in arr:
        if num in hashSet:
            hashSet[num] += 1
        else:
            hashSet[num] = 1

    
    sorted_items = sorted(hashSet.items(), key=lambda item: item[1], reverse=True)

    for key, value in sorted_items:
        selected.add(key)

        removed_count += value
        if removed_count >= len(arr) // 2:
            break

        
    return len(selected)


arr = [3,3,3,3,5,5,5,2,2,7]
print(reduceArray(arr))