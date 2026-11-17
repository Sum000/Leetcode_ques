class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # res = []
        # window_num = len(nums) - k + 1
        # for i in range(window_num):
        #     max_value = max(nums[i: i + k])
        #     res.append(max_value)

        # return res    

        # optimal approach

        


        res = []
        dq = deque()

        for r in range(len(nums)):

            #Remove indices outside the current window
            while dq and dq[0] <= r - k:
                dq.popleft()

            #Remove smaller or equal elements from the back
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            #Add the current index
            dq.append(r)

            # Record maximum once the first window is complete
            if r >= k - 1:
                res.append(nums[dq[0]])

        return res

       



        