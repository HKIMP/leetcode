## 分析

递归解法
```python

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        idx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        left = self.buildTree(preorder[1: idx+1], inorder[:idx])
        right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        root.left = left
        root.right = right

        return root
```