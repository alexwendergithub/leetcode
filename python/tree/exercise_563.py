# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.totalTilt = 0
        def calculate_sum_and_tilt(root):
            if root == None:
                return 0

            left_sum = calculate_sum_and_tilt(root.left)
            right_sum = calculate_sum_and_tilt(root.right)

            current_tilt = abs(left_sum - right_sum)
            self.totalTilt += current_tilt
            return left_sum + right_sum + root.val

        calculate_sum_and_tilt(root)
        return self.totalTilt