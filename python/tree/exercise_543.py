# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def measureDistance(root):
            if root is None:
                return 0
            left = measureDistance(root.left)
            right = measureDistance(root.right)

            current_diameter = left + right
            self.max_diameter = max(self.max_diameter, current_diameter)

            return 1 + max(left, right)

        measureDistance(root)
        
        return self.max_diameter