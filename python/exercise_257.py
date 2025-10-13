# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode],currentPath = None) -> List[str]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            if currentPath == None:
                return [str(root.val)]
            else:
                return [currentPath+"->"+str(root.val)]
        else:
            if currentPath == None:
                currentPath = str(root.val)
            else:
                currentPath = currentPath+"->"+str(root.val)
            pathsRight = self.binaryTreePaths(root.left,currentPath)
            pathsLeft = self.binaryTreePaths(root.right,currentPath)
            paths = pathsRight + pathsLeft
            return paths
