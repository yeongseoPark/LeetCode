class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return [strs]
        
        sorted_map = defaultdict(list)
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            
                # 무언가 답에 추가해주는 행위
            sorted_map[sorted_string].append(string)

        
        return list(sorted_map.values())