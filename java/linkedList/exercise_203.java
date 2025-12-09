/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode prev = null;
        ListNode headAux = head;
        while(headAux!=null){
            if(prev==null){
                if(head.val==val){
                    head = head.next;
                    headAux = headAux.next;
                }else{
                    prev = headAux;
                    headAux =headAux.next;
                }
            }else{
                if(headAux.val==val){
                    prev.next = headAux.next;
                    headAux = headAux.next;
                }else{
                    prev = headAux;
                    headAux = headAux.next;
                }
            }
        }
        return head;
    }
}