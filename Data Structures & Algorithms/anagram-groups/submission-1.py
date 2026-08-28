from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = defaultdict(list)

        for word in strs:
            sortedWords["".join(sorted(word))].append(word)

        returnableList = []

        for words in sortedWords.values():
            returnableList.append(words)

        return returnableList