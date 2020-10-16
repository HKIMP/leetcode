class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if l1 == None:return l2
        if l2 == None:return l1

        #将链表转换为数字(int)
        def listnode2num(node):
            res = 0
            while node:
                res = res * 10 + node.val
                node = node.next
            return res        

        result = listnode2num(l1) + listnode2num(l2)
        dummy_node = ListNode(-1)
        start_node = dummy_node
        for i in str(result):
            dummy_node.next = ListNode(int(i))
            dummy_node = dummy_node.next
        return start_node.next
