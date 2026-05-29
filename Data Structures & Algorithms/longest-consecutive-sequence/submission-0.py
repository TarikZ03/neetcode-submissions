class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        us_nums = sorted(set(nums))
        
        lengths = []
        counter = 1

        for i in range(len(us_nums)-1):
            if us_nums[i+1] - us_nums[i] == 1:
                counter += 1
            else:
                lengths.append(counter)
                counter = 1
                continue

        lengths.append(counter)
        return max(lengths)

