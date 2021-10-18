class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        for n in nums:
            if n == target or n > target:
                return count
            count += 1
        return count
