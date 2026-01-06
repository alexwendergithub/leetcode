# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hashmap = {}
    def findMode(self, root: Optional[TreeNode],value = 0) -> List[int]:
        if root!=None:
            if value == 0:
                self.hashmap = {}
            if root.val in self.hashmap:
                self.hashmap[root.val]+=1
            else:
                self.hashmap[root.val]=1
            self.findMode(root.left,1)
            self.findMode(root.right,1)
            res = []
            maxValue = 0
            if value == 0:
                for key in self.hashmap.keys():
                    if self.hashmap[key] > maxValue:
                        res = [key]
                        maxValue = self.hashmap[key]
                    elif self.hashmap[key] == maxValue:
                        res.append(key)
            return res
        else:
            return 0