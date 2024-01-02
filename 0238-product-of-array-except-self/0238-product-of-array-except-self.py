class Solution(object):
    def productExceptSelf(self, nums):
        
        n = len(nums)
        
        left_product = [0] * n
        right_product = [0] * n
        product_no_self = [0] * n
        
        left_product[0] = 1
        right_product[n-1] = 1
        
        for i in range(1, n):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
        
        for i in range(n):
            product_no_self[i] = right_product[i] * left_product[i]
        
        return product_no_self
        
                