class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l, r = 0, len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        curr_qty = 0

        while l < r:

            if maxLeft >= maxRight:

                r -= 1
                maxRight = max(maxRight, height[r])
                curr_qty += maxRight - height[r]

            else:
                l += 1
                maxLeft = max(maxLeft, height[l])
                curr_qty += maxLeft - height[l]

        return curr_qty
