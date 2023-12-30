class Solution(object):
    def containsDuplicate(self, nums):
        saw = {}
        for i in nums:
            if i in saw and saw[i] >= 1:
                return True 
            
            saw[i] = saw.get(i,0) + 1
        
        return False