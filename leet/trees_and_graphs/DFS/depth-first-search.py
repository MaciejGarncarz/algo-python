# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4686/

# Example of an recursion DFS

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None

input = TreeNode(0)
input.left = TreeNode(1)
input.left.left = TreeNode(3)
input.left.right = TreeNode(4)
input.left.right.right = TreeNode(6)
input.right = TreeNode(2)
input.right.right = TreeNode(5)

def recDfs(node: TreeNode) -> TreeNode:
    if node == None:
        return
    
    print(node.val)
    recDfs(node.left)
    recDfs(node.right)

print(recDfs(input))