class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        starting = 0
        ending = len(numbers) - 1

        while starting < ending:
            num1 = numbers[starting]
            num2 = numbers[ending]
            addition = num1 + num2

            if addition == target:
                return [starting+1, ending+1]
            elif addition < target:
                starting += 1
            else: 
                ending -= 1
            
        return [starting+1, ending+1]