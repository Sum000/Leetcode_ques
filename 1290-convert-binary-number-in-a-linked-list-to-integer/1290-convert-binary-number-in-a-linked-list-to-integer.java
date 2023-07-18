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
    public int getDecimalValue(ListNode head) {
        
        if (head.next == null)
            return head.val;
        
        int sum = 0;
        ListNode temp = head;
        int len = 1;
        
        while (temp.next != null){
            temp = temp.next;
            len++;
        }
        
        temp = head;
        
        while (temp != null){
            sum += temp.val * Math.pow(2, len-1);
            len--;
            temp = temp.next;
        }
        
        return sum;
            
        
    }
}