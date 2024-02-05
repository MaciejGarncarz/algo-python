# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4617/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tree = TreeNode(1)
# tree.right = TreeNode(2)
# tree.right.right = TreeNode(0)
# tree.right.right.right = TreeNode(3)

tree = TreeNode(8)
tree.left = TreeNode(3)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(6)
tree.left.right.left = TreeNode(4)
tree.left.right.right = TreeNode(7)
tree.right = TreeNode(10)
tree.right.right = TreeNode(14)
tree.right.right.right  = TreeNode(13)

# tree = TreeNode(2)
# tree.left = TreeNode(5)
# tree.right = TreeNode(0)
# tree.right.left = TreeNode(4)
# tree.right.left.right = TreeNode(6)
# tree.right.left.right.left = TreeNode(1)
# tree.right.left.right.left.left = TreeNode(3)



class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxDiff = 0

        def CheckInside(node: TreeNode) -> int:
            if node is None:
                return 0
            
            tempDiff = 0
            tempDiff = max(tempDiff, abs(root.val - node.val))
             

            rightDiff = CheckInside(node.right)
            leftDiff = CheckInside(node.left)

            tempDiff = max(tempDiff, rightDiff)
            tempDiff = max(leftDiff, tempDiff)

            return tempDiff


        # leftSide: TreeNode = root.left
        # while leftSide:
        #     if leftSide:
        #         maxDiff = max(maxDiff, abs(root.val - leftSide.val))
            
        #     if leftSide.left:
        #         leftSide = leftSide.left
        #     elif leftSide.right:
        #         leftSide = leftSide.right
        #     else:
        #         leftSide = None
        
        # rightSide: TreeNode = root.right
        # while rightSide:

        #     maxDiff = max(maxDiff, abs(root.val - rightSide.val))

            

        #     if rightSide.right:
        #         rightSide = rightSide.right
        #     elif rightSide.left:
        #         rightSide = rightSide.left
        #     else:
        #         rightSide = None

        rightTempDiff = CheckInside(root.right)
        leftTempDiff = CheckInside(root.left)

        maxDiff = max(rightTempDiff, maxDiff)
        maxDiff = max(leftTempDiff, maxDiff)


        right = self.maxAncestorDiff(root.right)
        left = self.maxAncestorDiff(root.left)

        temp = max(maxDiff, left)
        return max(temp, right)
    

solution = Solution()
print(solution.maxAncestorDiff(tree))


# class Solution:
#     def maxAncestorDiff(self, root: TreeNode) -> int:
#         if not root:
#             return 0

#         def helper(node, cur_max, cur_min):
#             # if encounter leaves, return the max-min along the path
#             if not node:
#                 return cur_max - cur_min
#             # else, update max and min
#             # and return the max of left and right subtrees
#             cur_max = max(cur_max, node.val)
#             cur_min = min(cur_min, node.val)
#             left = helper(node.left, cur_max, cur_min)
#             right = helper(node.right, cur_max, cur_min)
#             return max(left, right)

#         return helper(root, root.val, root.val)