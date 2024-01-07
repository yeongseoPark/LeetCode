class Solution(object):
    def longestConsecutive(self, nums):
        uniques = set(nums)
        ans = 0 
        
        while uniques:
            lo = hi = uniques.pop()
            
            while lo- 1 in uniques or hi + 1 in uniques:
                if lo - 1 in uniques:
                    uniques.remove(lo-1)
                    lo -= 1
                
                if hi + 1 in uniques:
                    uniques.remove(hi + 1)
                    hi += 1
            
            ans = max(ans, hi - lo + 1)
        
        return ans 