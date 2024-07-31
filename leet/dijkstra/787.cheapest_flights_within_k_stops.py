# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

from cmath import inf
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


from collections import defaultdict, deque
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        stops = [float('inf')] * n
        pq = [(0, src, 0)]  # (dist_from_src_node, node, number_of_stops_from_src_node)
        
        while pq:
            dist, node, steps = heapq.heappop(pq)
            
            if steps > stops[node] or steps > k + 1:
                continue
                
            stops[node] = steps
            if node == dst:
                return dist
            
            for neighbor, price in adj[node]:
                heapq.heappush(pq, (dist + price, neighbor, steps + 1))
        
        return -1

    

obj = Solution()

# n = 4
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]] 
# src = 0
# dst = 3 
# k = 1

# n = 5
# flights = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
# src = 0
# dst = 4 
# k = 1

n = 5
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1],[3,4,1]]
src = 0
dst = 4 
k = 2

print(obj.findCheapestPrice(n, flights, src, dst, k))

