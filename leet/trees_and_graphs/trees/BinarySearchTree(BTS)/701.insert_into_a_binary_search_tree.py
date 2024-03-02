# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


input = TreeNode(4, 
                 TreeNode(2, 
                          TreeNode(1), TreeNode(3)),
                TreeNode(7)
                 )


def insert_into_bts(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)

    if val > root.val:
        root.right = insert_into_bts(root.right, val)
        return root
    else:
        root.left = insert_into_bts(root.left, val)
        return root




result = insert_into_bts(input, 5)
print(result)
