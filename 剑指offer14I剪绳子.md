参考：
[图解【暴力递归】【记忆化技术】【动态规划】【动态规划优化解法】【找规律】](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/xiang-jie-bao-li-di-gui-ji-yi-hua-ji-zhu-dong-tai-/)

当n=1,2,3时，分隔后反而比没分割的值要小。


dp[i]表示长度为i的绳子的最大乘积
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[2] = 1
        for i in range(3, n+1):
            #i//2+1
            for j in range(i):
                dp[i] = max(dp[i], max((i-j)*j, dp[i-j]*j))
        return dp[n]
```