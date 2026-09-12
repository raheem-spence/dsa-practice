class Solution:
    def trap(self, height: List[int]) -> int:
        # given: an array of non-negatice integers height
        # goal: return the total amount of water that can be trapped between bars
        # pattern: two-pointers?
        
        l = 0

        r = len(height) - 1

        water = 0
        
        maxLeft = 0
        maxRight = 0

        while l < r:

            if height[l] <= height[r]:
                if height[l] >= maxLeft:
                    maxLeft = height[l]
                else:
                    water += maxLeft - height[l]
                
                l += 1
                
            else:
                if height[r] >= maxRight:
                    maxRight = height[r]
                else:
                    water += maxRight - height[r]
                r -= 1
                    
        return water
                
                