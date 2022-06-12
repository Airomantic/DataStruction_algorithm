class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


def creat_LinkList_head(li):
    head = ListNode(li[0])
    for element in li[1:]:
        node = ListNode(element)  # 注意是() 不是[] #相当于构建了一个self
        node.next = head  # 指向前一个输入的元素
        head = node  # 循环 新加入的元素成为新的头结点
    return head  # 逆序输出 li的元素


def creat_LinkList_tail(li):
    head = ListNode(li[0])
    tail = head  # 头指针和尾指针都指向第一个结点
    for element in li[1:]:
        node = ListNode(element)
        tail.next = node
        tail = node
    return head  # 依然返回head ，因为只有head才有next，tail已经指到最后面了


def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


lk = creat_LinkList_head([1, 2, 3])  # 3 —> 2 -> 1
# print(lk.item)
# print(lk.next.item)
print_linklist(lk)
print()
lk = creat_LinkList_tail([1, 2, 3, 6, 8, 9])  # 3 —> 2 -> 1
print_linklist(lk)
