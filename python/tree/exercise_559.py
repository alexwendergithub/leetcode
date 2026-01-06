"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        childMax = 0
        for chil in root.children:
            childMax = max(self.maxDepth(chil),childMax)
        return 1 + childMax
        