class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        choices = []

        indices = []
    
        for i, num in enumerate(nums):
            
            choices.append(num)
            indices.append(i)
    
            rem = target - num
    
            for j in range(i+1, len(nums)):
                if rem == nums[j]:
                    indices.append(j)
    
                    break
    
            if len(indices) != 2:
                choices.remove(num)
                indices.remove(i)
    
        
        return indices