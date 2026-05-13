import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hsh_set = {}

        for num in nums:
            hsh_set[num] = hsh_set.get(num, 0) + 1
        
        arr = []
        heapq.heapify(arr)

        for num, freq in hsh_set.items():
            heapq.heappush(arr, [freq, num])
        
            if len(arr) > k:
                heapq.heappop(arr)

        ans = []

        while arr:
            ans.append(heapq.heappop(arr)[1])

        return ans
        