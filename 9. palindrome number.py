from typing import List

# Given an integer x, return true if x is a palindrome, and false otherwise.
test_input = 121
expected_out = True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Its palindrome if reversed each value the output is same as input x.
        # Example: 121 is palindrome, -121 is not -> reversed: 121-
        # Take each num and reverse it, then append to string and compare with x.
        
        num_list = []
        number = ""
        for digit in str(x):
            num_list.append(digit)
        num_list.reverse()
        
        for num in num_list:
            number += num
        
        if str(x) == number:
            return True
        else:
            return False
        







                



            
            


solution = Solution()


result = solution.isPalindrome(test_input)
print(result) 