class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
    
    # Left to right pass
        count = 0  # Count of balls seen so far
        operations = 0  # Running sum of operations
        for i in range(n):
            answer[i] += operations
            count += int(boxes[i])
            operations += count
    
    # Right to left pass
        count = 0
        operations = 0
        for i in range(n-1, -1, -1):
            answer[i] += operations
            count += int(boxes[i])
            operations += count
    
        return answer