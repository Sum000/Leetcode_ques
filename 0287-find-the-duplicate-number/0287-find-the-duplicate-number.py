class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        num_map = set()
        for n in nums:
            if n in num_map:
                return n
            num_map.add(n)

        