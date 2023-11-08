class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_list = sorted(nums)
        max_sum = 0
        add_index = 0
        for i in range(len(nums) // 2):
            max_sum += min(sorted_list[i + add_index], sorted_list[i + 1 + add_index])
            add_index += 1
        return max_sum

nums = [1,1,2,2]


sol = Solution()
print(sol.arrayPairSum(nums))