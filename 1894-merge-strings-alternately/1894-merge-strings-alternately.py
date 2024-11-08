class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []  # List to store merged characters
        i, j = 0, 0  # Pointers for word1 and word2
    
    # Loop through both strings until one of them is exhausted
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])  # Add character from word1
            merged.append(word2[j])  # Add character from word2
            i += 1
            j += 1
    
    # Append remaining characters from the longer word, if any
        if i < len(word1):
            merged.extend(word1[i:])
        if j < len(word2):
            merged.extend(word2[j:])
    
    # Convert the list back to a string and return
        return ''.join(merged)