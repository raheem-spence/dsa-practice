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
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])

            if height[l] < height[r]:
                if l == 0:
                    l += 1
                    continue
                else:
                    if height[l] < maxLeft:
                        trapped = maxLeft - height[l]
                        water += trapped
                        l += 1
                    else:
                        l += 1
            else:
                if r == len(height) - 1:
                    r -= 1
                    continue
                else:
                    if height[r] < maxRight:
                        trapped = maxRight - height[r]
                        water += trapped
                        r -= 1
                    else:
                        r -= 1
        return water
                
                