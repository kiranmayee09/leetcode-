class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []

        total = 0

        for num in nums:
            total += num
            prefix.append(total)

        return prefix