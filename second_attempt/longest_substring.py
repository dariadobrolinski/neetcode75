class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        start = 0
        count = 0

        for i, char in enumerate(s):
            if char in hmap and hmap[char] >= start:
                start = hmap[char] + 1
            else:
                hmap[char] = i
                count = max(count, i - start + 1)

        return count

# July 30 2026