# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sets = []
        if head == None:
            return False
        while head.next != None:
            if head.next in sets:
                return True
            sets.append(head.next)
            head = head.next
        return False