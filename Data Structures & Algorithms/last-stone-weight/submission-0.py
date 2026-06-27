class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            n1 = heapq.heappop_max(stones)
            n2 = heapq.heappop_max(stones)
            if n1 == n2:
                continue
            n1 -= n2
            heapq.heappush_max(stones, n1)
        if stones:
            return stones[0]
        return 0
