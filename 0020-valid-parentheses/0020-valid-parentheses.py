class Solution(object):
    def isValid(self, s):
        opener = []
        
        
        
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                opener.append(ch)
            
            else:
                if ch == ")":
                    if len(opener) ==0 or opener.pop() != "(":
                        return False
                elif ch == "]":
                    if len(opener) ==0 or opener.pop() != "[":
                        return False
                elif ch == "}":
                    if len(opener) ==0 or opener.pop() != "{":
                        return False
                    
        if len(opener) != 0:
            return False
            
        return True