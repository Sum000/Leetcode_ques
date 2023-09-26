class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        m = len(nums1)
        n = len(nums2)
        for i in range(0,m) :
            k = 1
            index = nums2.index(nums1[i])
            while index + k < n:
                if nums1[i] < nums2[index + k]:
                    res.append(nums2[index + k])
                    break
                k += 1
            if index + k == n:
                res.append(-1)
                
        return res
                
            
        