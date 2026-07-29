class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j += 1
            i += 1

# O(n^2)
# date completed: July 23 2026