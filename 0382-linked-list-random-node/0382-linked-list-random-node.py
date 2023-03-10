# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        result, cur, idx = self.head, self.head.next, 1        
        while cur:
            if random.randint(0, idx) == idx:
                result = cur
            
            cur, idx = cur.next, idx+1
            
        return result.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()