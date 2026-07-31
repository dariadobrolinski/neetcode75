class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                current_sum = nums[left] + nums[right] + nums[i]
                if current_sum == 0:
                    solution.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

        return solution

# completed July 30 2026