class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        for i, t in enumerate(sorted([(d - 1) // s for d, s in zip(dist, speed)])):
            if i > t:
                return i
        return len(dist)    