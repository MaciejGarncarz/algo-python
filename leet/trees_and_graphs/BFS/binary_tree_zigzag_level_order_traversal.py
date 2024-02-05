# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4621/

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tree = TreeNode(3)
# tree.left = TreeNode(9)
# tree.right = TreeNode(20)
# tree.right.left = TreeNode(15)
# tree.right.right = TreeNode(7)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.right = TreeNode(5)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        level = 0 
        answer = []
        queue = deque([root])


        while queue:
            level += 1
            lenOfQueue = len(queue)
            levelOrder = []

            queue.reverse()
            for _ in range(lenOfQueue):
                node = queue.popleft()
                levelOrder.append(node.val)

                if level % 2 == 0:
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            answer.append(levelOrder)

        return answer



solution = Solution()
print(solution.zigzagLevelOrder(tree))