class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # brute force approach
        # n = len(nums)
        # res = [-1] * n

        # for i in range(n):

        #     for j in range(i + 1, i + n):

        #         idx = j % n
        #         if nums[idx] > nums[i]:
        #             res[i] = nums[idx]
        #             break

        # return res

        # optimal approach

        res = [-1] * len(nums)

        n = len(nums)

        stack = []

        for i in range(2*n - 1, -1, -1):

            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n:
                if stack:
                    res[i] = stack[-1]

            stack.append(nums[i % n])

        return res


        