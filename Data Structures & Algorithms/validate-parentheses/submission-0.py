class Solution:
    def isValid(self, s: str) -> bool:
                
        stack = []


        for char in s:
            # print(stack)
        
            if stack and ((char == "}" and stack[-1] == "{") or (char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "[")) :
                    # print(stack)
                    stack.pop()
                # stack.pop()

            else:
                stack.append(char)
        

        return False if (stack) else True 