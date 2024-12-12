from typing import List

test_input = "arc"
target_in = "arr"



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        anagram = list(t)
        word = list(s)

        if len(anagram) != len(word):
            return False
        
        count = 0
        for letter in word:
            if letter in anagram:
                anagram.remove(letter)
                count+=1
            
            else:
                return False
        
        if count == len(s):
            return True
            
        





        
                



            
            


solution = Solution()


result = solution.isAnagram(test_input, target_in)
print(result) 