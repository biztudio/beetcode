import pysnooper

class Solution:

    def EXPECTED_CONST(self):
        return 24

    @pysnooper.snoop()
    def check_validation(self, nums):
        return False    
    
    @pysnooper.snoop()
    def judgePoint24(self, nums) -> int:
        num_count = len(nums)
        if num_count < 1:
            return False
        if num_count == 1:
            return nums[0] == self.EXPECTED_CONST()

        return self.check_validation(nums)