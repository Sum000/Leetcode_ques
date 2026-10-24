class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # brute force solution

        # for i in range(len(nums)):
        #     total = nums[i]
        #     for j in range(i + 1, len(nums)):

        #         total += nums[j]
        #         if total % k == 0:
        #             return True

        # return False

        # optimal approach

        sum_map = {0:-1}

        total = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k
            if rem in sum_map:
                length = i - sum_map[rem]
                if length >= 2:
                    return True
            else:
                sum_map[rem] = i

        return False




        