class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        elif root.val >= low and root.val <= high:
            return root.val + self.rangeSumBST(root.right,low,high) + self.rangeSumBST(root.left,low,high)
        else:
            return self.rangeSumBST(root.right,low,high) + self.rangeSumBST(root.left,low,high)
