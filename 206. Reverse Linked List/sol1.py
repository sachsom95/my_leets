# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self, stack):
        if(len(stack) == 0):
            return
        else:
            node = ListNode()
            node.val = stack.pop()
            node.next = self.insert(stack)
        return node

    def reverseList(self, head: ListNode) -> ListNode:
        stk = []
        current_node = head
        while(current_node):
            stk.append(current_node.val)
            current_node = current_node.next

        return self.insert(stk)
