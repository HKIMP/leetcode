from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = dict()

        for i, num in enumerate(nums):
            d[num] = i
        
        for i in d:
            if target - i in d:
                return [d[i], d[target-i]]
        
        return None
        
if __name__ == '__main__':

    s = Solution()
    s.twoSum([3, 2, 4], 6)