class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def get_pop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


# 也可直接写一个list来运用栈结构
def match_brace(s):
    match = {'}': '{', ']': '[', ')': '('}  # 字典
    stack = Stack()

    for ch in s:
        if ch in {'{', '[', '('}:  # 集合（没有k-v）
            stack.push(ch)
        elif stack.get_pop() == match[ch]:
            stack.pop()
        else:  # stack.get_pop() != match[ch]:
            return False
    """最后进出栈为空是符合括号格式的关键点"""
    if stack.is_empty():
        return True
    return False


print(match_brace('[]{}{[]}'))
print(match_brace('[{'))