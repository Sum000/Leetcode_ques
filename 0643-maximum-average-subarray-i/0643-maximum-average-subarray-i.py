class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # brute force approach
        # res = float('-inf')
        # n = len(nums)
        # for i in range(n - k + 1):
        #     avg = sum(nums[i:k + i]) / k
        #     res = max(res, avg)

        # return res

        # optimal approach
        left, right = 0, k - 1
        window_sum = sum(nums[:k])
        max_sum = window_sum
        n = len(nums)
        for i in range(1, n - k + 1):
            new_sum = window_sum - nums[i - 1] + nums[i + k - 1]
            window_sum = new_sum
            max_sum = max(window_sum, max_sum)

        return max_sum / k



        