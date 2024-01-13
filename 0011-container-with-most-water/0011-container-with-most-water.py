class Solution(object):
    def maxArea(self, height):
        ans = 0 
        
        lo = 0
        hi = len(height) -1 
        
        while lo < hi:
            h = min(height[lo], height[hi])
            width = hi - lo
            ans = max(ans, h * width)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        
        return ans 
        
        
        