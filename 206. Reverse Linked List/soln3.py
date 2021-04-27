def rec(head):
    if (head.next):
        data = rec(head.next)
    else:
        return head
    head.next.next = head
    head.next = None
    return data
