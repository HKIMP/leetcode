#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = collections.defaultdict(int)

        left = right = 0
        res = 0
        max_count = 0
        
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            max_count = max(max_count, window[c])

            while right - left > max_count+k:
                d = s[left]
                window[d] -= 1
                left += 1
            res = max(res, right-left)
        return res
# @lc code=end

