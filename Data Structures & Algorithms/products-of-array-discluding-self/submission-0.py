class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroInList = False
        moreThanOneZeroInList = False
        numsLen = len(nums)

        finalProduct = 1

        for number in nums:
            if number == 0:
                if zeroInList == False:
                    zeroInList = True
                else:
                    moreThanOneZeroInList = True
                    return [0] * numsLen
            else:
                finalProduct *= number
        
        returnableList = [1] * numsLen

        if zeroInList == True:
            for i in range(numsLen):
                if nums[i] != 0:
                    returnableList[i] = 0
                else:
                    returnableList[i] = finalProduct
        
        else:
            for i in range(numsLen):
                returnableList[i] = int(finalProduct/nums[i])
        
        return returnableList
