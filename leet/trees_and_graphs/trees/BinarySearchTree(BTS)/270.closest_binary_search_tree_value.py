# https://leetcode.com/problems/closest-binary-search-tree-value/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


input = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))



def closest_value(root: Optional[TreeNode], target: float) -> int:
    answer = root.val
    minDifference = abs(root.val - target)
    if root is None:
        return answer
    
    def check_inside(node: Optional[TreeNode], answer:int, minDifference:float):
        if node is None:
            return answer
        
        if target > node.val:
            currentDifference = abs(node.val - target)
            if currentDifference < minDifference:
                answer = node.val
                minDifference = currentDifference
            if currentDifference == minDifference:
                answer = min(node.val, answer)
            return check_inside(node.right, answer, minDifference)
        else:
            currentDifference = abs(node.val - target)
            if currentDifference < minDifference:
                answer = node.val
                minDifference = currentDifference
            return check_inside(node.left, answer, minDifference)


    return check_inside(root, answer, minDifference)


closest_value(input, 3.7)
