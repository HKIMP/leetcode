from typing import List
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # need, window = {}, {}
        # # 
        # for c in s1:
        #     need[c] = need.setdefault(c, 0) + 1
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in s1:
            need[c] += 1
        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1

            # if c in need:
            if need[c] > 0:
                # window[c] = window.setdefault(c, 0) + 1
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left == len(s1):
                    return True
                d = s2[left]
                left += 1
                # if d in need:
                if need[d] > 0:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
if __name__ == '__main__':
    Solution().checkInclusion('ab', 'eidbaooo')