# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

from collections import defaultdict
from typing import List


def countComponents(n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    seen = set()
    answer = 0

    def dfs(node):
        for nextNode in graph[node]:
            if nextNode not in seen:
                seen.add(nextNode)
                dfs(nextNode)


    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)

    for x in range(n):
        if x not in seen:
            answer += 1
            dfs(x)


    return answer

n = 2
edges = [[1,0]]
print(countComponents(n, edges))
