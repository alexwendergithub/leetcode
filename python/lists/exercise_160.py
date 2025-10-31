# Possivel otimizar fazendo dois ponteiros percorrerem as duas listas em sequencia(eles se encontram em algum momento ou chegam no final juntos)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listaA = []
        while headA != None:
            listaA.append(headA)
            headA = headA.next
        while headB != None:
            if headB in listaA:
                return headB
            headB = headB.next
        return None