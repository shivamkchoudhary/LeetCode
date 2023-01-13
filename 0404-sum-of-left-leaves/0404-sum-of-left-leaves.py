# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def recursive(node):
            if node == None:
                return 0
            add = 0
            if node.left and node.left.left == None and node.left.right == None:
                add += node.left.val
                
            return add + recursive(node.left) + recursive(node.right)
        
        return recursive(root)