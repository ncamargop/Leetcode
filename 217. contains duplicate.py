from typing import List

# Given an integer x, return true if x is a palindrome, and false otherwise.
test_input = [2,3,1]
expected_out = True


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Brute force solution -> take each number and compare it with the rest.

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:  # Starting in pos 1, compare the first value i-1 with the actual.
                return True
        
        return False

         
            


solution = Solution()


result = solution.containsDuplicate(test_input)
print(result) 