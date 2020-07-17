# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        middle = 0
        current_node = head

        while(current_node.next):
            length += 1
            current_node = current_node.next
        length += 1
        if (length % 2 == 0):
            middle =int( (length/2)+1)
        else:
            middle =int( (length+1)/2)
        

        current_node = head
        
        while( middle > 1):
            current_node = current_node.next
            middle = middle -1
            
        print(current_node.val)
        return current_node

            
