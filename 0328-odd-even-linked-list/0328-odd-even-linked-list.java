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
    public ListNode oddEvenList(ListNode head) {
        ListNode odd = new ListNode(0);
        ListNode even = new ListNode(0);
        
        ListNode o = odd;
        ListNode e = even;
        ListNode temp = head;
        
        int index = 1;
        while (temp != null){
           
            if (index % 2 == 1){
                odd.next = temp;
                odd = odd.next;
                index++;
            }
            else{
                even.next = temp;
                even = even.next;
                index++;
            }
            temp = temp.next;
            
        }
        
        odd.next = e.next;
        even.next = null;
        
        return o.next;
        
    }
}