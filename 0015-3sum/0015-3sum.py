class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # without sorting
        # res = set()
        

        # for i in range(len(nums) - 2):
        #     seen = set()
        #     for j in range(i + 1, len(nums)):
        #         target = -(nums[i] + nums[j])
        #         if target in seen:
        #             triplet = tuple(sorted((nums[i],nums[j],target)))
        #             res.add(triplet)

        #         seen.add(nums[j])

        # return [list(x) for x in res]

        # two pointer approach
        nums.sort()
        res = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return res
                

                




        
        