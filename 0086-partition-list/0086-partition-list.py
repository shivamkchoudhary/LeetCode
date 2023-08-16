# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        bh = bt = ListNode()
        ah = at = ListNode()
        
        node = head
        while node:
            if node.val < x:
                bt.next = node
                bt = node
            else:
                at.next = node
                at = node
                
            node = node.next                
                
        at.next = None
        bt.next = ah.next
        
        return bh.next
        