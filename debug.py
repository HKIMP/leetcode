from typing import List

class Solution:
    def subsets(self, nums):
        size = len(nums)
        if size == 0:
            return []
        res = []        
        self.dfs(nums, 0, [], res)
        return res
    def dfs(self, nums, start, path, res):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i+1, path, res)
            path.pop()

ss = Solution()
res = ss.subsets([1, 2, 3])
