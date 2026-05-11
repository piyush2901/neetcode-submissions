class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ptr = 0

        right = len(numbers) - 1
        
        while ptr < right:
            if numbers[ptr] + numbers[right] > target:
                right -= 1

            elif numbers[ptr] + numbers[right] < target:
                ptr += 1
            
            else:
                return [ptr + 1, right + 1]