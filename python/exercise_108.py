# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left: int, right: int):
            if left > right:
                return None            
            mid = (left + right) >> 1

            root = TreeNode(
                val=nums[mid],
                left=buildBST(left, mid - 1),
                right=buildBST(mid + 1, right)
            )
            
            return root

        return buildBST(0, len(nums) - 1)