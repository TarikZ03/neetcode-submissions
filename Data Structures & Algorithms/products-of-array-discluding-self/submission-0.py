class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(len(nums)):
            if nums[i] != 0:
                running_prod = int(1)
                for j in range(len(nums)):
                    running_prod *= nums[j]
                output.append(running_prod // nums[i])
            else:
                running_prod = int(1)
                for j in range(len(nums)):
                    running_prod *= nums[j] if j != i else 1 
                output.append(running_prod)

        return output