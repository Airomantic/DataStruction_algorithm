"""
front 和 rear 依赖指针
队列的出队和进队特性实际上是：环形队列
注意⚠️：front 从来不指向元素（任何时候）
空队列：rear = front
队满 : rear + 1 = front
当加入新元素 rear指针后移一圈后超出就是MaxSize，采用 (rear + 1) % len(N) 转移到从0开始 这个len(N)就是MaxSize
环形队列: 当队尾指针 front == Maxsize+1 时,再前进一个位置就自动到0
队首指针前进1: front = (front+1)% Maxsize
队尾指针前进1: rear = (rear+1)% MaxSize
队空条件: rear == front
队满条件: (rear+1)% MaxSize == front

"""


class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear) + 1 % self.size  # 转化从0开始
            self.queue[self.rear] = element  # rear 指向新元素
        else: #注意这里的raise 只能依赖else，不能去掉else然后顶格写
            raise IndexError("Queue is filled!")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size  # 元素出队以后 front 也得往后以一个
            return self.queue[self.front]  # 任何时候都不指向元素，不管那里实际有没有元素，就不care
        raise IndexError("Queue is empty!")

    def is_empty(self):
        return self.rear == self.front

    """队满"""
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front  # front和rear之间隔了一个空格


q = Queue(5)  # 设置长度为5
for i in range(4):  # 长度为5的队列只能放4个元素，front和rear之间有个间隔
    q.push(i)

print(q.pop()) #先进先出
print(q.is_filled())