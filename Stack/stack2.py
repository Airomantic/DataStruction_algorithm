

# 也可直接写一个list来运用栈结构
def match_brace(s):
    match = {'}': '{', ']': '[', ')': '('}  # 字典
    stack=[]
    for ch in s:
        if ch in {'{', '[', '('}:  # 集合（没有k-v）
            stack.append(ch)
        elif stack[-1] == match[ch]:
            stack.pop()
        else:  # stack.get_pop() != match[ch]:
            return False
    """最后进出栈为空是符合括号格式的关键点"""
    if not stack:
        return True
    return False


print(match_brace('[]{}{[]}'))
print(match_brace('[{'))