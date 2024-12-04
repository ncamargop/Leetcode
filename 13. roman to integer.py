from typing import List

# Given string of roman letters give its numerical value
test_input = "LVIII"
expected_out = 58


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
        previous = 9999
        for letter in s:
            number = roman_letters.get(letter)
            
            if previous < number:
                rest = number - previous *2 # Its times 2 because in first pass we already added to count once, so we need to rest two times.
                count += rest
                
            else:
                count+= number

            print("prev: " + str(previous) + ", number: " + str(number) + ", count: " + str(count))
            previous = number
        

        return count


         
            


solution = Solution()


result = solution.romanToInt(test_input)
print(result) 