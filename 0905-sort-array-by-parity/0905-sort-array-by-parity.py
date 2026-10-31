class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l, r = 0, 1
        while l < r and r < len(nums):
            if nums[l] % 2 == 1:
                if nums[r] % 2 == 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r += 1

        return nums
            


             
            
        