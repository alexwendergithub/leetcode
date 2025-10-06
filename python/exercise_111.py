# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def searchLeaf(node):
            if node == None:
                return 0
            if node.left == None or node.right == None:
                return 1+searchLeaf(node.left)+searchLeaf(node.right)
            return 1+min(searchLeaf(node.left),searchLeaf(node.right))
        return searchLeaf(root)