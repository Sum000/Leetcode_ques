class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_i(arr):
            rob1, rob2 = 0, 0
            for n in arr:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        rob_x = rob_i(nums[:-1])
        rob_y = rob_i(nums[1:])
        return max(rob_x, rob_y)
        