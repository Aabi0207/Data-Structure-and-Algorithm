class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_list = sorted(nums)
        max_sum = 0
        for i in range(len(nums) // 2):
            max_sum += min()