class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(list(set(nums)))