## 分析 

这道题设计大数取余
而Python不涉及这个问题，故在结果直接取余。

根据推导，得出当绳子程度大于4的时候，
尽可能分成长度3的小段，这样乘积是最大的。
标准做法如下：

```python
class Solution:
    def cuttingRope(self, n: int):
        if n<=3:
            return n-1
        #必须有int，否则返回浮点型
        con = int(1e9+7)
        res = 1
        while n>4:
            n -= 3
            res = res*3%con
        return res*n%con
```

