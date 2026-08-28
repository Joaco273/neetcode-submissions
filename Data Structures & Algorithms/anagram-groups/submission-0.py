from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = defaultdict(list)

        for word in strs:
            sortedWords["".join(sorted(word))].append(word)

        return list(sortedWords.values())