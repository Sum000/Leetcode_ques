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
    public ListNode partition(ListNode head, int x) {
            if (head == null)
            return null;
        
        if (head.next == null)
            return head;
        
        ListNode small = new ListNode(0);
        ListNode big = new ListNode(0);
        
        ListNode s = small;
        ListNode b = big;
        
        ListNode temp = head;
        
        while (temp != null){
           if (temp.val < x){
               small.next = temp;
               small = small.next;
               
           } 
            else{
                big.next = temp;
                big = big.next;
            }
            temp = temp.next;
        }
        
        small.next = b.next;
        big.next = null;
        
        return s.next;
    }
}