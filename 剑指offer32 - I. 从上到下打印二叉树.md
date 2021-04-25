```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.pop(0)
                
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.extend(level)
        return res

```