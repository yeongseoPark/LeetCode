class Solution(object):
    def generateParenthesis(self, n):
        written = set()
        
        ans = [] 
        def dfs(left, right, path):
            if len(path) == n * 2:
                ans.append(path)
                return 
            
            if left >= right and left < n:
                dfs(left + 1, right, path + "(")
                dfs(left, right + 1, path + ")")
            elif right < n:
                dfs(left, right + 1, path + ")")
                
        dfs(0,0, "")
        return ans
        