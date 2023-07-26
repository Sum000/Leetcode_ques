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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        if (head == null || (head.next == null && n == 1))
            return null;
        
        
        ListNode temp = head;
        int len = 1;
        while (temp.next != null){
            temp = temp.next;
            len++;
        }
       
         temp = head;
        
        int t = len - n ;
        
        if (t < 0)
            return null;
        
        if (t == 0)
            return head.next;
        
        while (t != 1){
            temp = temp.next;
            t--;
        }
        
        temp.next = temp.next.next;
        
        return head;
        
    }
}