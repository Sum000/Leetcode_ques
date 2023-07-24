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
    public ListNode swapNodes(ListNode head, int k) {
        if (head.next == null)
            return head;
        
        int len = 1;
        ListNode temp = head;
        while (temp.next != null){
            temp = temp.next;
            len++;
        }
         int kEnd = len - k + 1;
        if (k == kEnd)
            return head;
        
        temp = head;
        ListNode temp2 = head;
        
        while (k > 1){
            temp = temp.next;
            k--;
        }
        
        while (kEnd > 1){
            temp2 = temp2.next;
            kEnd--;
        }
        
        int t;
        t = temp.val;
        temp.val = temp2.val;
        temp2.val = t;
        
        
       return head; 
        
    }
}