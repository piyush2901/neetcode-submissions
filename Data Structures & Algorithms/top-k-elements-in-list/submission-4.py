class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []

        hsh_set = {}
    
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            if num not in hsh_set:
                hsh_set[num] = hsh_set.get(num, 0) + 1
    
            else:
                hsh_set[num] += 1

        
        for num, freq in hsh_set.items():
            buckets[freq].append(num)

        # print(buckets)

        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for elem in buckets[i]:
                    ans.append(elem)
                if len(ans) == k:
                    return ans