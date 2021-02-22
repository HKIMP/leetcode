##bfs
```python

from collections import deque
class Solution:
    directions = [(1, 0), (0, 1)]
    def sum_rc(self, row, col):
        tmp = 0
        while row > 0:
            tmp += row % 10
            row //= 10
        while col > 0:
            tmp += col % 10
            col //= 10
        
        return tmp
    def movingCount(self, m: int, n: int, k: int) -> int:
        marked = set()
        queue = deque()
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()
            if (x, y) not in marked and self.sum_rc(x, y)<=k:
                marked.add((x, y))
                for dx, dy in self.directions:
                    if 0<=x+dx<m and 0<=y+dy<n:
                        queue.append((x+dx, y+dy))
        return len(marked)
```

## dfs
使用了闭包
```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sum_rc(x, y):
            tmp = 0
            while x > 0:
                tmp += x % 10
                x //= 10
            while y > 0:
                tmp += y % 10
                y //= 10
            return tmp
        
        def dfs(i, j):
            if i == m or j == n or sum_rc(i, j)>k or (i, j) in marked:
                return 
            marked.add((i, j))
            dfs(i+1,j)
            dfs(i, j+1)

        marked = set()
        dfs(0, 0)
        return len(marked)

```