from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        p = sorted(p)
        print(p)
        res = []
        for i in range(n - m + 1):
            sub = sorted(s[i : i + m])
            print(sub, p)
            if sub == p:
                res.append(i)
        return res

s = "abab"
p = "ab"
solution = Solution()
print(solution.findAnagrams(s, p))