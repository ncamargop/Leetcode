test_input = "([[])"
expected_out = True


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2 or s[0] in "]})":
            return False
        
        brackets = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        
        for char in s:    

            if char in "[{(": #Opening
                stack.append(char)
                continue

            
            if char in "]})":
                try:
                    opening = stack[-1]
                except IndexError:
                    return False

                if char == brackets.get(opening):
                    stack.pop()

                else:
                    return False
        
        if len(stack) > 0:
            return False
        
        else:
            return True






solution = Solution()


result = solution.isValid(test_input)
print(result) 