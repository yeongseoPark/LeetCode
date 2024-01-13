class Solution(object):
    def generateParenthesis(self, n):
        
        ans = []
        stack = [("(", 1, 0)]
        
        while stack:
            tmp = []
            
            for s, left, right in stack:
                if len(s) == 2 * n:
                    ans.append(s)
                    continue
                
                if left < n:
                    tmp.append((s + "(", left + 1, right))
                
                if left > right:
                    tmp.append((s + ")", left, right + 1))
                    
            stack = tmp 
        
        return ans 