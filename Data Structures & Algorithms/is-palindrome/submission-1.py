class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ""
        for char in s:
            if char.isalnum():
                sentence += char.lower()
        
        reversed_sentence = ''.join(reversed(sentence))

        if sentence == reversed_sentence:
            return True
        
        return False
        