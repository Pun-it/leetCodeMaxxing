class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = []
        len2 = []
        for i in nums1 :
            if i in nums2 :
                len1.append(i)
        for i in nums2 :
            if i in nums1:
                len2.append(i)
        return [len(len1),len(len2)]