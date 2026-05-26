class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        left = 0
        right = len(heights) - 1

        curr_max = 0

        while left < right:
            
            if heights[left] <= heights[right]:
                minHeight = heights[left]
                left += 1

            else:
                minHeight = heights[right]
                right -= 1
                
            curr_qty = minHeight*(right - left + 1)

            if curr_qty > curr_max:
                curr_max = curr_qty

        return curr_max


            