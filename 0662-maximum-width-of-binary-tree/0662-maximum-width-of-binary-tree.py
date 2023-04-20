# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans
        
        queue = collections.deque([(root, 0)])
        while queue:
            l, r = queue[0][1], queue[-1][1]
            ans = max(ans, r-l + 1)
            
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, idx*2+1))
                if node.right:
                    queue.append((node.right, idx*2+2))
                
        return ans
        