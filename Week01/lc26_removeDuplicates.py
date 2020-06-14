class Solution:
    def removeDuplicates1(self, nums):
        i = 0
        while(i<len(nums)-1):
            j = i+1
            if nums[i]==nums[j]:
                nums.remove(nums[j])
            else:
                i = i+1
                j = j+1
        return len(nums)
    
    def removeDuplicates2(self, nums):
        i = 0
        j = 1
        while(j<len(nums)):
            if nums[i]!=nums[j]:
                i = i+1
                nums[i] = nums[j]
            j = j+1
        return i+1

            
so = Solution()
a = [1,1,2,2,2,3,4,4,4,5]
print(so.removeDuplicates2(a))