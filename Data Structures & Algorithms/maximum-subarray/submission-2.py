[2,-3,4,-2,2,1,-1,4]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        # max_sum = max(nums)
        max_sum = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i]+dp[i-1], nums[i])
            max_sum = max(dp[i], max_sum) 
        return max_sum



        