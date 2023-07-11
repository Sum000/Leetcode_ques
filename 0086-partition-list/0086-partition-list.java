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
        
        ListNode temp = head;
        
        ListNode dummy = new ListNode(0);
        ListNode point = dummy;
        
        while (temp != null){
            if (temp.val < x){
               ListNode node = new ListNode(temp.val);
               point.next = node;
               point = point.next;
              
            }
            temp = temp.next;
        }
        
       temp = head;
        while (temp != null){
            if (temp.val >= x){
                ListNode node = new ListNode(temp.val);
                point.next = node;
                point = point.next;
            }
            temp = temp.next;
            
        }
        
        
        return dummy.next;
    }
}