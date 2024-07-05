# https://leetcode.com/problems/reachable-nodes-with-restrictions/description/

from collections import defaultdict
from typing import List


def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    graph = defaultdict(list)
    seen = set()
    answer = 0
    current_max = []

    def dfs(node):
        for nextNode in graph[node]:
            if nextNode not in seen:
                current_max.append(0)
                seen.add(nextNode)
                dfs(nextNode)


    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)

    for x in restricted:
        seen.add(x)

    dfs(0)
    answer = max(answer, len(current_max), 1)


    return answer

n = 10
edges = [[8,2],[2,5],[5,0],[2,7],[1,7],[3,8],[0,4],[3,9],[1,6]]
restricted = [9,8,4,5,3,1]

# n = 7 
# edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]] 
# restricted = [4,5]

# n = 7 
# edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
# restricted = [4,2,1]

print(reachableNodes(n, edges, restricted))