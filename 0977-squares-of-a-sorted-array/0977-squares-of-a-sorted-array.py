class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        k = right

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[k] = nums[left] ** 2
                left += 1

            else:
                res[k] = nums[right] ** 2
                right -= 1
            
            k -= 1

        return res

