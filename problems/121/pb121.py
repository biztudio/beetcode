import pysnooper

class Solution:
    
    @pysnooper.snoop()
    def lengthOfLIS(self, nums) -> int:
        '''
        关键：找它前面比他小的那些数中最大的
        状态的定义：以 num[i] 结尾的最长上升子序列的长度
        状态转移方程：之前的数中比 num[i] 小的最长上升子序列的长度 + 1
        '''
        num_count = len(nums)
        if num_count < 2:
            return num_count

        dp = [1 for num in nums]
        for num_index in range(1, num_count):
            for j in range(num_index):               
                if nums[num_index] > nums[j]:
                    dp[num_index] = max(dp[num_index], dp[j] + 1)

        return dp[-1]