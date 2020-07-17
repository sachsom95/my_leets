# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current_node = head
        while(head and head.val == val):
                if(current_node.next):
                    current_node = current_node.next
                    head = current_node
                else:
                    head = None
                    
        while(current_node and current_node.next):
                
            if(current_node.next.val == val):
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        
        return head
            
