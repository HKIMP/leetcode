# 思路一

1. 双指针headA, headB 分别指向A，B头结点
2. 分别逐个遍历两个链表。
3. 当headA到达末尾，重新定位到B链表头结点。
4. 当headB到达末尾，重新定位到A链表头结点。

## 分析
这个想法一开始确实没想到。。
1. 情况一：存在公共节点
   如果A的长度多l1+C, B的长度是l2+C。C为公共部分长度。A B长度不一样的话，首先要考虑互补彼此。
   因为两个指针需要一起走，所以互补的最基本方式就是公共都走(l1+l2)长度的节点，遍历到链表尾还得加C
   所以是(l1+l2+C)个长度
2. 情况二：不存在公共点
   headA headB分别遍历过彼此 最后None=None 退出循环 返回None

这样，当他们相遇，所指的结点就是第一个公共节点。

我们独自走过彼此的路，只要执手一次，从此与君偕老。
哎。。。上代码
```python
class Solution:
    def getIntersectionNode(self, headA:ListNode, headB:ListNode)->ListNode:
        
        ListNode1 = headA
        ListNode2 = headB

        while ListNode1 != ListNode2:
            ListNode1 = ListNode1.next if ListNode1!= None else headB
            ListNode2 = ListNode2.next if ListNode2!= None else headA
            
        return ListNode1
```
