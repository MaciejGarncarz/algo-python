# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right = TreeNode(3)


class Solution:
    diameter = 0 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def countDepth(node: TreeNode):
            if not node:
                return 0
            
            left = countDepth(node.left)
            right = countDepth(node.right)

            total = (right + left)
            self.diameter = max(self.diameter, total)

            return max(left, right) + 1
        
        countDepth(root)
    
        return self.diameter

sol = Solution()
print(sol.diameterOfBinaryTree(tree))