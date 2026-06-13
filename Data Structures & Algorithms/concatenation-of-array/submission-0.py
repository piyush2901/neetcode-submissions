import copy

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = copy.deepcopy(nums)

        for num in nums:
            ans.append(num)

        return ans