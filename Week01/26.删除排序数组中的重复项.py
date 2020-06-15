#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while(j<len(nums)):
            if nums[i]!=nums[j]:
                i = i+1
                nums[i] = nums[j]
            j = j+1
        return i+1
# @lc code=end

