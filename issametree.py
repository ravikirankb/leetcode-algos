# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p and q:
           if p.val != q.val:
               return False
            
        else:
            return False
        
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        
