# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4620/

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        answer = 0
        queue = deque([root])
        
        while queue:
            queueLen = len(queue)
            answer = 0
            
            for _ in range(queueLen):
                node = queue.popleft()
                answer += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return answer
        