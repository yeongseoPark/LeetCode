class Solution(object):
    def productExceptSelf(self, nums):
        
        n = len(nums)
        
        product_no_self = [1] * n
        
        for i in range(1, n):
            product_no_self[i] = product_no_self[i-1] * nums[i-1]
        
        right = 1
        for i in range(n-1, -1, -1):
            product_no_self[i] *= right
            right = right * nums[i]
            
        return product_no_self
                