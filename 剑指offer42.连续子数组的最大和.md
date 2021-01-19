## 分析

主要是找对dp数组，本地dp数组的定义是：

以nums[i]为结尾的‘最大子数组和’为dp[i]

时间：O(N)
空间: O(1)

```python
class Solution:
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp_0 = nums[0]
    dp_1 = 0
    res = dp_0
    for i in range(1, n):
        dp_1 = max(nums[i], dp_0+nums[i])
        dp_0 = dp_1
        res = max(dp_1, res)
    return res
```