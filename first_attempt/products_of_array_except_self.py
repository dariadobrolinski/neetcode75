class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [0] * len(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            sol[i] = product
        return sol

# O(n^2)
# date completed: July 28th 2026