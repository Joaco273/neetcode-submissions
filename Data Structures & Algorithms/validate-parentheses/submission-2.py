class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in matching:
                if stack:
                    value = stack.pop()
                else: 
                    return False

                if value != matching [char]:
                    return False
                
            else:
                stack.append(char)
        
        return len(stack) == 0