import pysnooper
from fractions import Fraction

class Solution:

    def EXPECTED_CONST(self):
        return 24

    #@pysnooper.snoop()
    def check_validation(self, nums, expected):
        num_count = len(nums)
        validation = False
        if num_count < 1:
            return validation
        if num_count == 1:
            return nums[0] == expected
        
        ref_index = 0
        calculation = 0
        for ref_num in nums[:-1]:
            if validation:
                break
            else:
                cal_index = ref_index + 1
                for cal_num in nums[cal_index:]:

                    if ref_index != cal_index:

                        next_nums = [nums[i] for i in range(num_count) if i != cal_index and i != ref_index]

                        if validation == False:
                            calculation = ref_num + cal_num
                            next_nums.append(calculation)
                            validation = validation or self.check_validation(next_nums, expected)
                            next_nums.pop()

                        if validation == False:
                            calculation = ref_num - cal_num
                            next_nums.append(calculation)
                            validation = validation or self.check_validation(next_nums, expected)
                            next_nums.pop()

                        if validation == False:
                            calculation = cal_num - ref_num
                            next_nums.append(calculation)
                            validation = validation or self.check_validation(next_nums, expected)
                            next_nums.pop()


                        if validation == False:
                            calculation = ref_num * cal_num
                            next_nums.append(calculation)
                            validation = validation or self.check_validation(next_nums, expected)
                            next_nums.pop()


                        if validation == False and cal_num != 0:
                            calculation = Fraction(ref_num, cal_num)
                            next_nums.append(calculation)
                            validation = validation or self.check_validation(next_nums, expected)
                            next_nums.pop()


                        if validation == False and  ref_num != 0:
                            calculation = Fraction(cal_num, ref_num)
                            next_nums.append(calculation)
                            validation = validation or self.check_validation(next_nums, expected)
                            next_nums.pop()


                    cal_index = cal_index + 1

                ref_index = ref_index + 1

        return validation
    
    #@pysnooper.snoop()
    def judgePoint24(self, nums) -> int:
        return self.check_validation(nums, self.EXPECTED_CONST())