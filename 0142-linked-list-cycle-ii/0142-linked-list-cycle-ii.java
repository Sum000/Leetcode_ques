/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null)
            return null;
        
        ListNode slow = head;
        ListNode fast = head;
        ListNode entry = head;
      
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if (fast == slow)
                break;
        }
        
        if (fast != slow)
            return null;
        
            while (entry != slow){
                
                entry = entry.next;
                slow = slow.next;
            }
            return entry;
        
      
        
    }
}