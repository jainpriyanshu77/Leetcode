class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

    # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != 0:  # If the current element is non-zero
            # Swap the elements at the current index and the non-zero index
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            # Move the non-zero index forward
                non_zero_index += 1

    # # Iterate through the array from right to left
    #     for i in range(len(nums) - 1, -1, -1):
    #         if nums[i] == 0:  # If the current element is zero
    #         # Swap it with the element at zero_index
    #             nums[zero_index], nums[i] = nums[i], nums[zero_index]
    #         # Move zero_index to the left
    #             zero_index -= 1
 