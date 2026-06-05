class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1
        solution = []

        while i<j:
            
            #if the sum is too big then move to the next smaller number in the list
            if numbers[i] + numbers[j] > target:
                j -= 1

            #if the sum is too small then move to the next bigger number in the list
            elif numbers[i] + numbers[j] < target:
                i += 1

            #if the sum is equal to the target then just return the solution
            else:
                return [i+1, j+1]
        

        return solution