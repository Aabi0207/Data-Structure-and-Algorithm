class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_data = len(nums1) + len(nums2)
        if merged_data == 0:
            return None
        median = 1
        for i in range(1, merged_data):
            median += 0.5
        return median


nums1 = []
nums2 = []

sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))
