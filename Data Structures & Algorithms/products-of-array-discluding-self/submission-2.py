class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1

        output = [1]*len(nums)
    
        for i in range(1, len(nums)):
            curr_pre = nums[i - 1]
            prefix *= curr_pre
            output[i] = prefix
    
        postfix = 1
    
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
    
        return output
    