import pysnooper

class Solution:
    
    @pysnooper.snoop()
    def majorityElement(self, nums) -> int:
        '''
        常见算法思路为摩尔投票算法
        '''
        num_count = len(nums)
        if num_count < 1:
            return num_count
        if num_count == 1:
            return nums[0]    

        check_flag = 0
        temp_check_num = nums[0]
        for num in nums:
            
            if num == temp_check_num:
                check_flag = check_flag + 1
            else:
                check_flag = check_flag - 1            
                if check_flag == 0:
                    temp_check_num = num
                    check_flag = check_flag + 1

        return temp_check_num