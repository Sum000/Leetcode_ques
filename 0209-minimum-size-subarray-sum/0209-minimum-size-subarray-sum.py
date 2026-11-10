class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # brute force appraoch

        #  res = float('inf')

        # for i in range(len(nums)):
        #     current_sum = 0

        #     for j in range(i, len(nums)):
        #         current_sum += nums[j]

        #         if current_sum >= target:
        #             res = min(res, j - i + 1)
        #             break

        # return 0 if res == float('inf') else res

        # optimal approach


        left = 0
        total = 0
        res = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                res = min(res, right - left + 1)

                total -= nums[left]
                left += 1

        return 0 if res == float('inf') else res



