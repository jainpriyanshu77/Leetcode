class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        equal = []
        greater = []

        for n in nums:
            if n > pivot:
                greater.append(n)

            elif  n < pivot:
                less.append(n)

            else:
                equal.append(n)
        less.extend(equal)
        less.extend(greater)
        return less

