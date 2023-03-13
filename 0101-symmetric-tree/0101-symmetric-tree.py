# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True        
        stack = [(root.left, root.right)]
     
        while stack:
            nodes = stack.pop()
			
            l, r = nodes

            if l is None and r is None: 
                continue  
            if l is None or r is None:
                return False

            if l.val != r.val:  
                return False

            stack.append((l.right,r.left))
            stack.append((l.left,r.right))
                
        return True