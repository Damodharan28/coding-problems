# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None : return 0 

        mx_left = self.maxDepth(root.left)
        mx_right = self.maxDepth(root.right)

        return max(mx_left, mx_right) + 1
