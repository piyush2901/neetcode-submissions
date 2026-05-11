class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hsh_set = defaultdict()

        for i, num in enumerate(nums):
            hsh_set[num] = i

        for i, num in enumerate(nums):
            if target - num in hsh_set and hsh_set[target - num] != i:
                return [i, hsh_set[target - num]]

        return []