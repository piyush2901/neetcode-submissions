class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                if len(stack) >= 2:
                    secondNum = stack.pop()
                    firstNum = stack.pop()
                    if token == "+":
                        res = int(firstNum) + int(secondNum)
                    elif token == "-":
                        res = int(firstNum) - int(secondNum)
                        
                    elif token == "*":
                        res = int(firstNum) * int(secondNum)

                    else:
                        res = int(firstNum) / int(secondNum)


                    stack.append(res)
            else:
                stack.append(token)
        
        return int(stack[-1])