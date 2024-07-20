# https://leetcode.com/problems/all-paths-from-source-to-target/description/

from collections import defaultdict
from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    answer = []

    def backtrack(curr: List[int], i: int):
        if curr[-1] == len(graph) - 1:
            answer.append(curr[:]) # curr[:] is a copy of curr since arrays are passed by reference
            return
        
        for node in graph[i]:
            curr.append(node)
            backtrack(curr, node)
            curr.pop()
            



    backtrack([0], 0)
    return answer
    
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(allPathsSourceTarget(graph))