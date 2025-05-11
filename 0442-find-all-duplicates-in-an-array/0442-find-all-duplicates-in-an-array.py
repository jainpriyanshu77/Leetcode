class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for num in nums:
            at_index = nums[abs(num) - 1]

            if at_index < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return res