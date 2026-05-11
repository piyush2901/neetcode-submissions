class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsh_set = set(nums)

        if len(hsh_set) < len(nums):
            return True

        return False

