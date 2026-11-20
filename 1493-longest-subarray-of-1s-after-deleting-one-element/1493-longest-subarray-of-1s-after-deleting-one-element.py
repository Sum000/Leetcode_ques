class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # brute force approach

        # res = 0

        # for i in range(len(nums)):
        #     count_zero = 0
        #     count_one = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] == 1:
        #             count_one += 1
        #             res = max(res, count_one)
        #         else:
        #             count_zero += 1

        #         if count_zero > 1:
        #             break
            
        #     if count_one == len(nums):
        #         return len(nums) - 1


        # return res


        # optimal approach

        l, r = 0, 0
        res = 0
        count_zero = 0

        while r < len(nums):
            if nums[r] == 0:
                count_zero += 1

            while count_zero > 1:
                if nums[l] == 0:
                    count_zero -= 1

                l += 1

            if count_zero <= 1:
                res = max(res, r - l)

            r += 1

        return res



                

        