# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4691/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

# tree = TreeNode(2)
# tree.right = TreeNode(3)
# tree.right.right = TreeNode(4)
# tree.right.right.right = TreeNode(5)
# tree.right.right.right.right = TreeNode(6)


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        if(root.left == None):
            return self.minDepth(root.right) + 1
        
        if(root.right == None):
            return self.minDepth(root.left) + 1
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1
    
solution = Solution()
print(solution.minDepth(tree))