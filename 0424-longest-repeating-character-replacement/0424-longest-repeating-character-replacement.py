class Solution:
    def characterReplacement(self, s, k):
        lo = 0
        hi = 0
        letters = {}
        ans = 0
        max_letter_cnt = 0  # 윈도우 안에서 가장 빈번한 글자의 개수

        while hi < len(s):
            letters[s[hi]] = letters.get(s[hi], 0) + 1 # hi로 인해 추가된 윈도우 안의 새 문자 letters에 기록
            max_letter_cnt = max(max_letter_cnt, letters[s[hi]])

            # 다른게 넘 많아서 한칸 줄여줌(lo쪽을)
            if (hi - lo + 1) - max_letter_cnt > k:
                letters[s[lo]] -= 1
                lo += 1

            ans = max(hi-lo+1, ans)
            hi += 1
        return ans 