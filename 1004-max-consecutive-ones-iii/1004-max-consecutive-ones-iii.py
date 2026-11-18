class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # brute force approach
        # res = 0
        # for i in range(len(nums)):
        #     zeros = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] == 0:
        #             zeros += 1

        #         if zeros <= k:
        #             res = max(res, j - i + 1)
        #         else:
        #             break
                

        # return res



        # optimal approach

        max_len, zeros = 0, 0
        l, r = 0, 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            if zeros <= k:
                max_len = max(max_len, r - l + 1)

            r += 1

        return max_len


        

        
        