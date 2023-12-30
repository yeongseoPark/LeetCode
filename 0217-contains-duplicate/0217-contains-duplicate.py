class Solution(object):
    def containsDuplicate(self, nums):
        set_nums = list(set(nums))

        if len(nums) - len(set_nums) > 0:
            return True
        else:
            return False 
        
        