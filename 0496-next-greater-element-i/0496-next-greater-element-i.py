class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n = len(nums2)
        for num in nums1:
            k = 1
            index = nums2.index(num)
            while index + k < n:
                if num < nums2[index + k]:
                    res.append(nums2[index + k])
                    break
                k += 1
            if index + k == n:
                res.append(-1)
                
        return res
                
            
        