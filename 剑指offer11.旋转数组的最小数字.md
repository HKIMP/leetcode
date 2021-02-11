## 分析

二分法
```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        size = len(numbers)
        if size == 0:
            return 0
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] == numbers[right]:
                right -= 1
            else:
                right = mid
        return numbers[left]
``