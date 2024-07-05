#https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from collections import defaultdict
from typing import List


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    answer = False

    def dfs(node):
        if destination in graph[node]:
            nonlocal answer
            answer = True
            return
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    if len(graph) == 0:
        graph[0].append(0)

    seen = set()

    
    dfs(source)
    return answer

n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
source = 5
destination = 9

result = validPath(n, edges, source, destination)
print(result)




