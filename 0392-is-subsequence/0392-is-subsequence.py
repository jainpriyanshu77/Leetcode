class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
            # left, right = s[0], t[0]
            # while s < t:
            #     if s == t:
            #         s+= 1
            #     else:
            #         t += 1
            # return true
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        sub = 0

        for i in range(0, len(t)):
            if sub <= len(s) - 1:
                print(s[sub])
                if s[sub] == t[i]:
                    sub += 1
        return sub == len(s)