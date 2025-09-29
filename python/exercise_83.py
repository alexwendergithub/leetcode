# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        headAux = head
        while headAux != None and headAux.next != None:
            if headAux.next.val == headAux.val:
                aux = headAux.next.next
                del(headAux.next)
                headAux.next = aux
            else:
                headAux = headAux.next
        return head