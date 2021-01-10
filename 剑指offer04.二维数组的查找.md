## 分析

此题关键 是 怎么样有效缩减 二维数组的范围，最终找到target。

四个方位：
1. 左上角：向下 向右 都变大 
2. 右上角：向下变大 向左变小
3. 左下角：向右边大 向上变小
4. 右下角：向上变小 向左边小
   
需要的不是 左上角 这种类型。向下，向右都变大 到底向哪里呢？

所以可以选择右上 或 坐下。

右下代码如下：

时间复杂度:(O(M+N)) 访问到的下标的行最多增加 n 次，列最多减少 m 次，因此循环体最多执行 n + m 次。
空间复杂度:O(1)
```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        n = len(matrix) # 行数
        m = len(matrix[0]) #列数

        row = 0
        column = m-1

        while row <n and column >= 0:
            if target == matrix[row][columu]:
                return True
            elif target < matrix[row][column]:
                column -= 1
            else:
                row += 1
        return False
```


