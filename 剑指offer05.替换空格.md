## 分析 

## 参考
1. [面试题05. 替换空格 （字符串修改，清晰图解）](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/solution/mian-shi-ti-05-ti-huan-kong-ge-ji-jian-qing-xi-tu-/)

采用python实现，书上的方法适用于c++。因为c++的string是可变类型，可以在不新建

字符串的情况下实现原地修改。

而Python的情况是字符串是不可变类型，不能在原字符串修改，必须生成新串。

所以这道题用Python实现的话，不能用书上的方法。

```python

class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)
```

