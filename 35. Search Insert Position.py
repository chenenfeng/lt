"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""


# my program seems low efficient, a lot of if determine which position the target should insert
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if i == len(nums)-1:
                return i+1
            if nums[i] < target:
                if nums[i+1] > target:
                    return i+1
                    
# look at this one, share a high efficient solve way
# https://leetcode.com/problems/search-insert-position/discuss/165424/Super-simple-Python-20ms-100
 
"""
my thought is imprisoned.. I should have think once I found the first one bigger than target, then insert target
who cares the previous one, it definetly smaller than target because I just find the first bigger one, just insert
if no found, just insert target to the last one
"""
