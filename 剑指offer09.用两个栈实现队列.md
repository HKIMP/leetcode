## 分析

注意删除元素

如果B不为空，直接返回B.pop()

如果B为空，讨论

第一种情况A为空，返回-1

第二种情况A不为空，则把A的元素放进B里，在弹出B的栈顶元素
```python
class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
```