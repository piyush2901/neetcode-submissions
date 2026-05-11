class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hsh_set = set()

        for num in nums:
            if num in hsh_set:
                return True

            hsh_set.add(num)

        return False
