# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSymmetrical(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        print([p.val,q.val])
        return self.isSameTree(p.left,q.right) and (p.val == q.val) and self.isSameTree(p.right,q.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        return self.isSymmetrical(root.left,root.right)