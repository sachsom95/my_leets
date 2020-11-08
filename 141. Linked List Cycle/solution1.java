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
    public boolean hasCycle(ListNode head) {
        
        if(head == null) return false;
        
        var slow = head;
        var fast = head;
        
        while(fast.next != null && fast.next.next != null)
        {
            
            slow = slow.next;
            fast = fast.next.next;
            if( fast == slow ) return true;
        
        } 
        return false;
    }
}
