class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        max_len = 0
        chars = set()
        lo = 0

        for hi in range(len(s)):
            if s[hi] not in chars: 
                chars.add(s[hi])
                max_len = max(max_len, hi - lo + 1)
            else: # 중복 발생
                while s[hi] in chars: # 중복되는게 substring 안에 없을때까지 
                    chars.remove(s[lo]) # 중복을 제거하고
                    lo += 1 # 시작점을 높임
                chars.add(s[hi]) # 시작점이 다시 정해졌으니 여기서부터 다시 길이재기 시작

        return max_len