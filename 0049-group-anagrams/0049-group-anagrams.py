class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return [strs]
        
        sorted_map = {}
        ans = []
        
        for string in strs:
            sorted_string = str(sorted(string))
            
            
            if sorted_string in sorted_map:
                # 무언가 답에 추가해주는 행위
                sorted_map[sorted_string].append(string)
            
            else:
                sorted_map[sorted_string] = [string]
        
        for key in sorted_map.keys():
            ans.append(sorted_map[key])
        
        return ans