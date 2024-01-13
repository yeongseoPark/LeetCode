class Solution(object):
    def threeSum(self, nums):
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return [] 
        
        nums.sort()
        
        ans = []
        
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            
            lo = idx + 1
            hi = len(nums) - 1
            while lo < hi:
                s = nums[idx] + nums[lo] + nums[hi]
                if s == 0:
                    ans.append([nums[idx], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                    
                elif s < 0:
                    lo += 1 
                else:
                    hi -= 1
        return ans 