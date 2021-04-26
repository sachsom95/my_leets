class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        temp = None
        while (current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev
        return head
