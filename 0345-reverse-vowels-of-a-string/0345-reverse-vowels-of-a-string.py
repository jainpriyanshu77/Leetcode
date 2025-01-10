class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        st = 0
        end = len(s) - 1 
        vowels = "aeiouAEIOU"

        while st  < end:
            while st  < end and vowels.find(word[st]) == -1:
                st += 1

            while st  < end and vowels.find(word[end]) == -1:
                end -= 1
            word[st], word[end] =  word[end], word[st]

            st += 1
            end -= 1

        return "".join(word)