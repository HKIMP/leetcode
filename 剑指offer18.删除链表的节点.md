## 分析

这道题和剑指offer有出入。
差别在于leetcode的val是值
剑指offer是节点val
本地解法为：
```python
class Solution:
    def deleteNode(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        if head.val == val:
            return head.next
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            head = head.next
        return dummy.next
```

剑指offer写法：
```python
class Solution:
def deleteNode(self, head, val):
    if head is None or val is None:
        return None
    
    #待删除的不是尾结点
    if val.next is not None:
        tmp = val.next
        val.val = tmp.val
        val.next = tmp.next
    #待删除的节点只有一个节点，这个节点是头结点
    elif head == val:
        head = None
    #待删除的节点为尾结点
    else:
        cur = head
        while cur.next!=val:
            cur = cur.next
        cur.next = None
    return head
```















