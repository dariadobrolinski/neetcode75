class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        
        for i in range(len(nums)):
            if nums[i] not in hset:
                hset.add(nums[i])
            else:
                return True
        return False

# completed July 29 2026