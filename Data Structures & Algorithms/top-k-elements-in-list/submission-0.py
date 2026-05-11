class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []

        hsh_set = {}
    
        for num in nums:
            if num not in hsh_set:
                hsh_set[num] = hsh_set.get(num, 0) + 1
    
            else:
                hsh_set[num] += 1
    
        hsh_set = sorted(hsh_set.items(), key= lambda x : x[1], reverse= True)    
    
    
        for i in range(1, k + 1):
            ans.append(hsh_set[i - 1][0])
    
    
        return ans