class Solution(object):
    def dailyTemperatures(self, temp):
        ans = [0] * len(temp)
        
        stack = []
        
        for i, t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        
        return ans
                