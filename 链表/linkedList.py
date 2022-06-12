class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

print(a.next.item)
print(a.next.next.item)