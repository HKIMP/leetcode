```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        flag = 0
        while queue:
            n = len(queue)
            level = []

            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
               
            if flag % 2 == 0:
                res.append(level)
            else:
                res.append(level[::-1])
            flag += 1
        return res
```