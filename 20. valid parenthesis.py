test_input = "([])"
expected_out = False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False
        for char in s:
            
            
            if stack:
                if char in "}])":
                    if char == ")" and stack[-1] == "(":
                        stack.pop()
                        continue
                    
                    if char == "]" and stack[-1] == "[":
                        stack.pop()
                        continue

                    if char == "}" and stack[-1] == "{":
                        stack.pop()
                        continue
                    
                    else:
                        print(char)
                        return False
                
                else: return False
            
            
            if char in "[{(": #Opening
                stack.append(char)
                continue

                
        return True
            
            


            
                    
                
            

      






solution = Solution()


result = solution.isValid(test_input)
print(result) 