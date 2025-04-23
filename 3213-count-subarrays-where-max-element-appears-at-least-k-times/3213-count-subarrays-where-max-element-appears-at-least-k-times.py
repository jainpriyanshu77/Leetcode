class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_num = max(nums)
        n = len(nums)
        count = 0
        left = 0
        max_count = 0

        for right in range(n):
            if nums[right] == max_num:
                max_count += 1

            while max_count >= k:
                count += (n - right)
                if nums[left] == max_num:
                    max_count -= 1
                left += 1

        return count
