# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        return self.helper(root.right,val) and self.helper(root.left,val)
     
    
    def helper(self,root,val):
        if root is None:
            return True
        
        if root.val != val:
            return False
        
        return self.helper(root.right,val) and self.helper(root.left,val)
        
        
