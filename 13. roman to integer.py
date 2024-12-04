from typing import List

# Given an integer x, return true if x is a palindrome, and false otherwise.
test_input = "IV"
expected_out = 1994


class Solution:
    def romanToInt(self, s: str) -> int:
        # Use dict for each letter and store its value
        # Then for each character in 's' get the value from dict and sum.

        roman_letters = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        count = 0
        previous = ""
        num_to_rest = 0
        prev_conditioned = None
        for letter in s:
            
            number = roman_letters.get(letter)
            
            
            """if previous == "X" and (letter == "L" or letter == "C"):
                rest = (number-10)

            if previous == "C" and (letter == "D" or letter == "M"):
                rest = (number-100)"""


            if letter in ["I", "X", "C"] and prev_conditioned == False and previous not in ["I", "X", "C"]:
                prev_conditioned = True
                num_to_rest = roman_letters.get(letter)
            
            else:

                prev_conditioned = False
                previous = letter
                count += (number-num_to_rest)

                

            

            
            
            


        print("final:" + str(count))

        



            
            


solution = Solution()


result = solution.romanToInt(test_input)
print(result) 