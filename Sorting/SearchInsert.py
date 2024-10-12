class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        d = target
        while i <= len(nums)-1:
            if nums[i] == target:
                return i
            if nums[i] < target:
                d = i
            i += 1
        if target < nums[0]:
            return 0
        else: return d + 1