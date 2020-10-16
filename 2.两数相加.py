class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkList():

    def __init__(self, node=None):
        self.head = node
    
    def add(self, list):
        for val in list[::-1]:
            new_code = ListNode(val)
            new_code.next = self.head
            self.head = new_code

    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.val, end='->')
            cur = cur.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy_node = ListNode(-1)
        start_node = dummy_node
        #记录进位
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum = num1 + num2 + carry

            carry = sum // 10
            mod = sum % 10

            l1 = l1.next if l1!= None else None
            l2 = l2.next if l2!= None else None

            #尾插法
            new_node = ListNode(mod)
            dummy_node.next = new_node
            dummy_node = new_node

        return start_node.next

s1 = SingleLinkList()
s1.add([2, 4, 3])
s2 = SingleLinkList()
s2.add([5, 6, 4])
s1.travel()
print()
s2.travel()
sol = Solution()
result = sol.addTwoNumbers(s1.head, s2.head)
s3 = SingleLinkList()
s3.head = result
print()
s3.travel()
