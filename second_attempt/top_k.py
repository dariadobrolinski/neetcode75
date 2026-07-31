class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        solution = []

        for num in nums:
            hmap[num] += 1

        heap = [(-val, key) for key, val in hmap.items()]
        heapq.heapify(heap)

        for _ in range(k):
            val, key = heapq.heappop(heap)
            solution.append(key)
        
        return solution

# July 30 2026