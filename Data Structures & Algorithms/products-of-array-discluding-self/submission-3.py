class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        hsh_set = defaultdict(list)
        
        ans = []

        curr_prod = 1

        n = len(nums)

        for i in range(n):    
            curr_prod *= nums[i]
            hsh_set[i].append(curr_prod)

        curr_prod = 1
        for i in range(n-1, -1, -1):    
            curr_prod *= nums[i]
            hsh_set[i].append(curr_prod)

        for i in range(n):
            if i == 0:
                ans.append(hsh_set[i + 1][1])
            elif i == n - 1:
                ans.append(hsh_set[i-1][0])
            else:
                ans.append(hsh_set[i-1][0] * hsh_set[i+1][1])

        return ans