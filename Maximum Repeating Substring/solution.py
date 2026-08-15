class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        t,res = word,0
        while t in sequence:
            res += 1
            t += word
        return res
