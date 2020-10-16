class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkList():

    def __init__(self, node=None):
        self.head = node
    
    def add(self, item):
        node = ListNode(item)
        node.next = self.head
        self.head = node

    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.val)
            cur = cur.next
    

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, p = None, head
        while p:
            next = p.next
            p.next = prev
            prev = p
            p = next
        return prev


sl = SingleLinkList()
sl.add(1)
sl.add(2)
sl.add(4)
sl.travel()
sol = Solution()
rev = sol.reverseList(sl.head)
s1 = SingleLinkList(node=rev)
s1.travel()
# print(rev.val)
# print(rev.next.val)
# print(rev.next.next.val)
