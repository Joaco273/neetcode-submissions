class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        curr_numbers = []

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token == '+':
                num1 = int(curr_numbers.pop())
                num2 = int(curr_numbers.pop())
                result = num2+num1
                curr_numbers.append(result)
            elif token == '-':
                num1 = int(curr_numbers.pop())
                num2 = int(curr_numbers.pop())
                result = num2-num1
                curr_numbers.append(result)
            elif token == '*':
                num1 = int(curr_numbers.pop())
                num2 = int(curr_numbers.pop())
                result = num2*num1
                curr_numbers.append(result)
            elif token == '/':
                num1 = int(curr_numbers.pop())
                num2 = int(curr_numbers.pop())
                result = int(num2/num1)
                curr_numbers.append(result)
            else:
                curr_numbers.append(token)
                
        
        return result