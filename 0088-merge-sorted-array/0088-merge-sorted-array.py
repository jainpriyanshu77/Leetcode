class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1  

    # Traverse nums1 and nums2 from the end
        while i >= 0 and j >= 0:  
        # Compare the last elements of nums1 and nums2
            if nums1[i] > nums2[j]:  
                nums1[k] = nums1[i]  # Place the larger element at the end of nums1
                i -= 1  # Move the nums1 pointer left
            else:
                nums1[k] = nums2[j]  # Place the larger element from nums2 at the end of nums1
                j -= 1  # Move the nums2 pointer left
            k -= 1  # Move the position pointer left

    # If nums2 still has elements left, copy them (nums1 elements are already in place)
        while j >= 0:  
            nums1[k] = nums2[j]  # Copy remaining elements from nums2 to nums1
            j -= 1  # Move nums2 pointer left
            k -= 1 