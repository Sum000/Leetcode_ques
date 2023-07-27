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
    public ListNode sortList(ListNode head) {
        // base case
        if (head == null || head.next == null)
            return head;
        
        //split list into two halfs
        ListNode left = head;
        ListNode right = getMiddle(head);
        ListNode temp = right.next;
        right.next = null;
        right = temp;
        left = sortList(left);
        right = sortList(right);
        return merge(left, right);
    }
    
   public ListNode getMiddle(ListNode head){
        ListNode slow = head;
        ListNode fast = head.next;
        
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
       return slow;
    }
    
    public ListNode merge(ListNode list1, ListNode list2){
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (list1 != null && list2!= null){
            if (list1.val < list2.val){
                tail.next = list1;
                list1 = list1.next;
            }
            else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        
        if (list1 != null){
            tail.next = list1;
            list1 = list1.next;
            tail = tail.next;
        }
        
        if (list2 != null){
            tail.next = list2;
            list2 = list2.next;
            tail = tail.next;
        }
        
        return dummy.next;
    }
}