# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode],isLeft = False) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            if isLeft:
                return root.val
            else:
                return 0
        else:
            return self.sumOfLeftLeaves(root.left,True) + self.sumOfLeftLeaves(root.right,False)