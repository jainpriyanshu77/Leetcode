class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        hash = {'(': ')','{':'}', '[':']'}
        stack = []
        for c in s:
            if c in hash:
                stack.append(c)
            elif len(stack) == 0 or hash[stack.pop()] != c:
                return False
        return len(stack) == 0


