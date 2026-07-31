class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for left in range(len(s)):
            charSet = set()
            for right in range(left, len(s)):
                if s[right] in charSet:
                    break
                charSet.add(s[right])
                longest = max(longest, len(charSet))
        return longest