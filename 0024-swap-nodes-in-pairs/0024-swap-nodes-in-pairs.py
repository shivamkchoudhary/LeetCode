# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, head)
        prev, curr= temp, head
        
        
        while curr and curr.next:
            #save
            nextPair = curr.next.next
            second = curr.next
            
            #reverse
            second.next = curr
            curr.next = nextPair
            prev.next = second
            
            #update
            prev = curr
            curr = nextPair
        
        return temp.next
        