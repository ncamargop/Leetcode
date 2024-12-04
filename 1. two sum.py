from typing import List

test_input = [2,5,5,11]
target_in = 10
expected_out = [0,1]

# Temporal complexity: O(N^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Take first element of the list and compare it with the others
        # until the sum is equal to target, then break

        for i in range(0, len(nums)):
            base_num = nums[i]

            for j in range(i+1, len(nums)):
                if (base_num + nums[j] == target):
                    return [nums.index(base_num), j] # Return the position of elements
                



            
            


solution = Solution()


result = solution.twoSum(test_input, target_in)
print(result) 