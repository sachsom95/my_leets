# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if (head):
            fast = head
            slow = head
            is_even = False
            lst = []
            is_pal = False
            lst.append(head.val)
            while(fast.next and fast.next.next):
                fast = fast.next.next
                slow = slow.next
                lst.append(slow.val)
            
            if(fast.next):
                is_even = True
                # print("is even")
                # print("lst",lst)
            
            if(is_even):
                slow = slow.next
                while(slow):
                    if(slow.val != lst.pop()):
                        # print(f"1 slow.val{slow.val} lst.pop:{lst}")
                        return False
                    else:
                        # print(f"2 slow.val:{slow.val} lst:{lst}")
                        slow = slow.next
            else:
                slow = slow.next
                lst.pop()
                while(slow):
                    if(slow.val != lst.pop()):
                        return False
                    else:
                        slow = slow.next
            return True
        else:
            return True
            
            
            
        
