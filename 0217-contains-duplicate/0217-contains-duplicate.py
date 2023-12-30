class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i]:
                return True
        
        return False 
        
        