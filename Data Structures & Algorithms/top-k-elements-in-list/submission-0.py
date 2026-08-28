class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for number in nums:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1
        
        sorted_by_value = (sorted(frequency.items(), key=lambda item: item[1], reverse = True))

        returnableList = []
        for i in range(k):
            returnableList.append(sorted_by_value[i][0])

        return returnableList