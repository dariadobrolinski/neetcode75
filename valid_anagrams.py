class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for letter in s:
            if letter in hmap:
                hmap[letter] += 1
            else:
                hmap[letter] = 1
        
        for letter in t:
            if letter in hmap:
                hmap[letter] -= 1
            else:
                return False

        for key, value in hmap.items():
            if value != 0:
                return False

        return True

# O(n + m), n = len(s), m = len(t)
# date completed: July 23 2026