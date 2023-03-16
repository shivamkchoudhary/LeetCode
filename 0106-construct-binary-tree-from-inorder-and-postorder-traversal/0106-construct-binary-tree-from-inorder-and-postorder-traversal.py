# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            root_idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_idx])
            root.right = self.buildTree(inorder[root_idx+1:], postorder)
            root.left = self.buildTree(inorder[:root_idx], postorder)
            return root
        