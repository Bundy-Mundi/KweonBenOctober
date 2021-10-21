class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            if nums[i] == 0:
                c = i
                for j in range(c+1, len(nums)):
                    if nums[j] != 0:
                        temp = nums[j]
                        nums[j] = nums[c]
                        nums[c] = temp
                        c+=1
