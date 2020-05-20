# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:  
        output =[]
        output = self.helper(root,output)
        return output[k-1]
        
    def helper(self,root,output):
        if not root:
            return 
        if root.left:
            self.helper(root.left,output)
        output.append(root.val)
        if root.right:
            self.helper(root.right,output)
        return output
