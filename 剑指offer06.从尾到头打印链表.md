## 分析

书上做法
```python

class Solution:
    def reversePrint(self, head):
        res = []
        if not head:
            return res
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            res.append(stack.pop())
        return res

```
或者
```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        return res[::-1]
```