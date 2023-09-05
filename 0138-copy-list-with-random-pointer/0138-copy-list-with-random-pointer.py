"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head): # -> 'Node':
        memo = {}
        def deepcopy(n):
            if not n:
                return
            if n in memo:
                return memo[n]
            memo[n] = new = Node( n.val )
            new.next   = deepcopy(n.next  )
            new.random = deepcopy(n.random)
            return new
        return deepcopy(head)
        