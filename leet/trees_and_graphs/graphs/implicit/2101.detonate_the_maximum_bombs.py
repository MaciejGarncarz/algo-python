# https://leetcode.com/problems/detonate-the-maximum-bombs/description/

from collections import defaultdict, deque
from typing import List


def maximumDetonation(bombs: List[List[int]]) -> int:
    graph = defaultdict(list)
    n = len(bombs)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            xi, yi, ri = bombs[i]
            xj, yj, _ = bombs[j]
                
            if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                graph[i].append(j)

    
    answer = 0
    def bfs(i):
        queue = deque([i])
        visited = set([i])
        while queue:
            cur = queue.popleft()
            for neib in graph[cur]:
                if neib not in visited:
                    visited.add(neib)
                    queue.append(neib)
        return len(visited)
    
    for x in range(n):
        answer = max(answer, bfs(x))
    
    return answer

bombs = [[2,1,3],[6,1,4]]

print(maximumDetonation(bombs))