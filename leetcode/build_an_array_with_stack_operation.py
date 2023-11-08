class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        
        stack = []
        for i in range(1, n + 1):
            if i in target:
                stack.append("Push")
            if i < target[-1] and i not in target:
                stack.append("Push")
                stack.append("Pop")
        return stack

target = [1,3]
n = 3
sol = Solution()
print(sol.buildArray(target, n))