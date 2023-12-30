class Solution(object):
    def twoSum(self, nums, target):
        wife = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num in wife:
                return [i, wife[num]]
            
            wife[target-num] = i
        
        
        