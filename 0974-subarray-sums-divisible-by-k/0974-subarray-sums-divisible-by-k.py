class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res, total = 0, 0
        num_map = {0:1}

        for n in nums:
            total += n
            rem = total % k
            if rem in num_map:
                res += num_map[rem]
                num_map[rem] += 1
            else:
                num_map[rem] = 1

        return res