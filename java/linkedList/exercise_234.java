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
    public boolean isPalindrome(ListNode head) {
        List<Integer> lista = new ArrayList<>();
        ListNode headAux = head;
        int count = 0;
        while(headAux != null){
            lista.add(0,headAux.val);
            headAux = headAux.next;
        }
        int[] numbersArray = lista.stream().mapToInt(i -> i).toArray();
        for(int i=0;i<lista.size()/2;i++){
            if(head.val != numbersArray[i]){
                return false;
            }
            head = head.next;
        }
        return true; 
    }
}