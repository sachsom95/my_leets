# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        len = 0
        sum = 0
        current_node = head
        while(current_node):
            len += 1
            current_node = current_node.next
        
        current_node = head
        len = len - 1
        while(current_node):
            sum = sum + (current_node.val*(2**len))
            len -= 1
            current_node = current_node.next
        return sum



