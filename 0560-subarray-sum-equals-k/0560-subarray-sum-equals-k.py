class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force approach.

        # res = 0

        # for i in range(len(nums)):
        #     total = nums[i]
        #     if total == k:
        #         res += 1
        #     for j in range(i + 1, len(nums)):
        #         total += nums[j]
        #         if total == k:
        #             res += 1

        # return res

        res, total = 0, 0

        sum_map = {0:1}

        for n in nums:
            total += n
            diff = total - k
            res += sum_map.get(diff, 0)
            sum_map[total] = sum_map.get(total, 0) + 1


        return res



        





       

        
        