class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        solution = 0       

        for i in range(len(prices)):
            low = prices[i]
            for j in range(i + 1, len(prices)):
                high = prices[j]
                solution = max(solution, high - low)
        
        return solution

# completed July 29 2026