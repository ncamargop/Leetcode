from typing import List

test_input = [0,1,2,2,2,2,2,3,4,4,4]



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j = 0
        k = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                nums[j] = "x"
                nums.append("_")
            
            else:
                k+=1
            
            j+=1
        
      
        
        while "x" in nums:
            nums.remove("x")

        return k+1


        

        
    

        
            

        


        
            
    
            
            


solution = Solution()


result = solution.removeDuplicates(test_input)
print(result) 