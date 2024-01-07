class Solution(object):
    def longestConsecutive(self, nums):
        dic = {}
        for num in nums:
            dic[num] = 1
        
        ans = 0
        for num in nums:
            if num- 1 not in dic:
                cnt = 1
                tmp = num + 1
                while tmp in dic:
                    cnt += 1
                    tmp += 1
                
                dic[num] = cnt
                ans = max(ans, cnt)
        
        return ans
            