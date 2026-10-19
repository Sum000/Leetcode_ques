class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        left_total, right_total = 0, 0
        for i in range(n):
            if i == 0:
                continue
            else:
                left_total += nums[i - 1]
                left_sum[i] = left_total

        for j in range(n - 1, -1, -1):
            if j == n - 1:
                continue
            else:
                right_total += nums[j + 1]
                right_sum[j] = right_total
    
        for i in range(n):
            if left_sum[i] == right_sum[i]:
                return i

        return -1


        