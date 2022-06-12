"""
单链表
插入: 必须先将要插入的元素的指针先指向要插入某元素之后的元素，如插入 curNone -> nextNone 之间，再将当前节电的指针指向插入元素，以作为前节点
颠倒顺序，会导致后面的元素游失到内存里面
p.next = curNode.next
curNone.next = p
删除：
p = curNode.next （表示想把curNode后面那个节点删掉）
curNode.next = curNode.next.next (或者写= p.next)
del p （可写可不写）

双链表
插入
p.next = curNode.next
curNode.next.prior = p
p.prior = curNode
curNode = p
删除：
p = curNode.next   (表示想把curNode后面的元素删了)
curNode.next = p.next
p.next.prior = curNode
del p

查找：list: O(1)  链表：O(n)
链表的内存可以更灵活的分配
链表实现队列不会出现队满
"""