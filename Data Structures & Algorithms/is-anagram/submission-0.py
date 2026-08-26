class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqA = {}
        freqB = {}

        for letter in s:
            if (letter in freqA):
                freqA[letter] += 1
            else:
                freqA[letter] = 1

        for letter in t:
            if (letter in freqB):
                freqB[letter] += 1
            else:
                freqB[letter] = 1

        return freqA == freqB