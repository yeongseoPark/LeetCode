class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        chars = [0] * 26
        
        for i in range(len(s)):
            chars[ord(s[i]) - 97] += 1
            chars[ord(t[i]) - 97] -= 1
        
        for i in chars:
            if i != 0:
                return False
        
        return True