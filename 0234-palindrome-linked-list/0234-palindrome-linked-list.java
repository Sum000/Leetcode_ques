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
       
        if (head.next == null)
            return true;
        
        ListNode fast = head;
        ListNode slow = head;
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        
        while (fast != null  && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            prev = prev.next;
        }
        prev.next = null;
        ListNode revHead = reverse(slow);
        
        ListNode list1 = dummy.next;
        ListNode list2 = revHead;
        
        while (list1 != null && list2 != null) {
            if (list1.val != list2.val)
                return false;
            list1 = list1.next;
            list2 = list2.next;
        }
        
        
        return true;
    }
    public static ListNode reverse(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;
        
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        
        return prev;
    }
}