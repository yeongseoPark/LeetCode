from heapq import heappush, heappop
class Solution(object):
    def topKFrequent(self, nums, k):
        count_map = defaultdict(int)
        que = []
        
        for num in nums:
            count_map[num] += 1
        
        for key,val in count_map.items():
            heappush(que, (-val, key))
        
        ans = []
        for _ in range(k):
            ans.append(heappop(que)[1])
        
        return ans