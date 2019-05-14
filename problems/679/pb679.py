import pysnooper
from fractions import Fraction

class Solution:

    def EXPECTED_CONST(self):
        return 24

    @pysnooper.snoop()
    def check_validation(self, nums, expected):
        num_count = len(nums)
        if num_count < 1:
            return False
        if num_count == 1:
            return nums[0] == expected
        validation = False

        new_expected = expected + nums[0]
        validation = validation or self.check_validation(nums[1:], new_expected)

        new_expected = expected - nums[0]
        validation = validation or self.check_validation(nums[1:], new_expected)

        new_expected = nums[0] - expected
        validation = validation or self.check_validation(nums[1:], new_expected)

        new_expected = expected * nums[0]
        validation = validation or self.check_validation(nums[1:], new_expected)

        if nums[0] != 0:
            new_expected = Fraction(expected, nums[0]) 
            validation = validation or self.check_validation(nums[1:], new_expected)  

        if expected != 0:
            new_expected = Fraction(nums[0], expected) 
            validation = validation or self.check_validation(nums[1:], new_expected)  

        return validation    
    
    @pysnooper.snoop()
    def judgePoint24(self, nums) -> int:
        return self.check_validation(nums, self.EXPECTED_CONST())