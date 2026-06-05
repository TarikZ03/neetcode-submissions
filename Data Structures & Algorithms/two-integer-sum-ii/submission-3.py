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

            elif numbers[i] + numbers[j] == target and i<j and i != j:

                solution.append(i+1)
                solution.append(j+1)
                return solution
        

        return solution