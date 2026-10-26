class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        total, res = 0, 0
        num_map = {0:1}

        for n in nums:
            total += n
            k = total - goal
            res += num_map.get(k,0)
            num_map[total] = num_map.get(total, 0) + 1

        return res
            

        return res
        