class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += str(len(word)) + "|" + word
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0
        lenOfString = len(s)

        while i < lenOfString:
            j=i
            while s[j] != "|":
                j+=1
            length = int(s[i:j])
            decodedString.append(s[j+1 : j+1+length])
            i = j+1+length
        return decodedString
