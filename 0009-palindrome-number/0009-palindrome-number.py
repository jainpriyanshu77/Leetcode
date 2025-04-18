class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digits = []
        temp = x
        while temp > 0:
            digits.append(temp % 10)
            temp = temp //10
        return digits == digits[::-1]