class Solution(object):
    def findMin(self, nums):
        # 일단 정상 array로 만들고 이분탐색?
        lo = 0 
        hi = len(nums) - 1
        
        maxval = nums[-1]

        while lo < hi:
            mid = (lo + hi) //2
            
            if nums[mid] > nums[hi]:
                lo = mid + 1
            
            else:
                hi = mid
            
        return nums[hi]
                
            
                


        