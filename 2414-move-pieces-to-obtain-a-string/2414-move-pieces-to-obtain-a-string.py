class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start) != len (target):
            return False

        if start.replace('_', '' ) != target.replace('_', '' ):
            return False

        n = len(start)
        j = 0

        for i  in range(n):
            if start[i] == 'L' or start[i] == 'R':
                while j < n and target[j] == '_':
                    j += 1

                if start[i] == 'L' and i < j:
                    return False

                if start[i] == 'R' and i > j:
                    return False

                j+=1
        
        return True