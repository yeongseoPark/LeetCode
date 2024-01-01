from heapq import heappush, heappop
class Solution(object):
    def topKFrequent(self, nums, k):
        count_map = defaultdict(int)
        que = []
        
        for num in nums:
            count_map[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key,value in count_map.items():
            bucket[value].append(key)
        
        ans = []
        for i in range(len(nums), -1, -1):
            if bucket[i] != []:
                ans += bucket[i]
            
        return ans[:k]