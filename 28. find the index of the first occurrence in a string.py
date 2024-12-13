# find index of first occurence of needle in haystack
needle = "ll"
haystack = "hello"



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i = 0
        count = len(needle)
        while i in range(0, len(haystack)):
            if haystack[i:count] == needle:
                return i

            else:
                i+= 1
                count += 1
        
        return -1

                




            

        
         
            


solution = Solution()


result = solution.strStr(haystack, needle)
print(result) 