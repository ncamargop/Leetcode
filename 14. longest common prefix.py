from typing import List

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


test_input = ["flower", "flight"]
expected_out = "fl"


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest = strs[0]
        
        for i in range(1, len(strs)):
            while not strs[i].startswith(longest):
                longest = longest[:-1]  # Remove the last character from the prefix
                if longest == "":
                    return ""
        
        return longest
        

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars = zip(*strs)
        #zip(*strs) takes all the strings in strs and groups their characters by position
        # strs = ["flower", "flow", "flight"]
        # zip(*strs) = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ...]
        
        res = ""

        for c in chars:
            if len(set(c)) == 1:  # len(set(c)) -> takes each in chars and removes duplicates. If all characters are the same, the set will have only one element.
                # If only one element in each position then add to res.
                res += c[0]
            else:
                break
        return res
    

        

        
            
    

         
            


solution = Solution2()

 
result = solution.longestCommonPrefix(test_input)
print(result) 