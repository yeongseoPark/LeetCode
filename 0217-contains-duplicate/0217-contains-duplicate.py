class Solution(object):
    def containsDuplicate(self, nums):
        saw = set()
        for i in nums:
            if i in saw:
                return True 
            
            saw.add(i)
        
        return False