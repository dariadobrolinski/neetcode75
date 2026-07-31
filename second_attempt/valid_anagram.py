class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        for char in s:
            if char not in hmap:
                hmap[char] = 1
            else: 
                hmap[char] += 1
        
        for char in t:
            if char not in hmap:
                return False
            else:
                hmap[char] -= 1

        for key, value in hmap.items():
            if value != 0:
                return False
    
        return True

# completed July 29 2026