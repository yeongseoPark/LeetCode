class Solution(object):
    def twoSum(self, numbers, target):
        lo = 0
        hi = len(numbers)-1
        
        while True:
            if numbers[lo] + numbers[hi] == target:
                return [lo + 1, hi + 1]
                break
            
            elif numbers[lo] + numbers[hi] < target:
                lo += 1
            
            else:
                hi -= 1
        
        return ans 
        