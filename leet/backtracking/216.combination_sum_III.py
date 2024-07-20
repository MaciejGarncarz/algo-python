# https://leetcode.com/problems/combination-sum-iii/description/

from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    answer = []

    def backtrack(path: List[int], sum: int, index: int):
        if len(path) == k:
            answer.append(path[:])
            return
        
        for number in range(index, 10):
            if len(path) < k-1:
                path.append(number)
                backtrack(path, sum + number, number + 1)
                path.pop()
            else:
                if sum + number == n:
                    path.append(number)
                    backtrack(path, sum + number, number + 1)
                    path.pop()
    
    backtrack([], 0, 1)
    return answer


print(combinationSum3(3, 7))