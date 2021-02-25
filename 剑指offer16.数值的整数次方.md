## 分析

利用快速幂的方法
```python
class Solution:
    def myPow(self, x, n):
        if x == 0:
            return 0
        res = 1
        if n<0:
            n = -n
            x = 1 / x
        while n:
            if n % 2:
                res *= x
            x *= x
            n >>= 1
        return res
```