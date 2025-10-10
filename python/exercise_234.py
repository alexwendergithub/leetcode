#fazer em O(n) time e O(1) space depois usando fast and slow pointer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lista = []
        headAux = head
        count = 0
        while headAux != None:
            lista.insert(0,headAux.val)
            headAux = headAux.next
        for i in range(int(len(lista)/2)):
            if head.val != lista[i]:
                return False
            head = head.next
        return True