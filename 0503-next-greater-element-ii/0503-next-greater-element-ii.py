class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # brute force approach
        n = len(nums)
        res = [-1] * n

        for i in range(n):

            for j in range(i + 1, i + n):

                idx = j % n
                if nums[idx] > nums[i]:
                    res[i] = nums[idx]
                    break

        return res

        # optimal approach
        


        