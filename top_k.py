class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        sol = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(heap)

        for _ in range(k):
            val, key = heapq.heappop(heap)
            sol.append(key)
        
        return sol