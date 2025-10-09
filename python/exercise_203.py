# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        p = None
        q = head
        while q != None:
            if q.val == val:
                if p == None:
                    head = head.next
                    q = q.next
                else:
                    p.next = q.next
                    q = q.next
            else:
                p = q
                q = q.next
                
            
        return head