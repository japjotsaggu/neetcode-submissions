class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count, curr_count = 0, 0 

        for i in range(len(nums)):
            num = nums[i]

            if num-1 not in set_nums:
                curr_count = 1
                while num+1 in set_nums:
                    curr_count+=1 
                    num+=1 
                    max_count = max(max_count, curr_count)

        return max(max_count, curr_count)

