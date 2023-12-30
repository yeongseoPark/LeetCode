class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        