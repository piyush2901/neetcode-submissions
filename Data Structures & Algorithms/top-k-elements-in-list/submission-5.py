class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hsh_set = {}

        for num in nums:
            hsh_set[num] = hsh_set.get(num, 0) + 1
        

        arr = []
        for num, freq in hsh_set.items():
            arr.append([freq, num])

        arr.sort()

        ans = []
        while len(ans) < k:
            ans.append(arr.pop()[1])

        return ans