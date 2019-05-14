from behave import given, when, then, step
from  pb679 import Solution
from fractions import Fraction

@given(u'Input {nums_string}')
def step_impl(step, nums_string):
    step.nums_string = (nums_string)

@when(u'Calculate')
def step_impl(step):  
    calKit = Solution()
    nums = [int(c) for c in step.nums_string.split(",")]
    step.calculated_result =  calKit.judgePoint24(nums)  

@then(u'Get Result {validation}')
def step_impl(step, validation):
    #validate_math = 4 / (1 - Fraction(2,3))
    #print('4 / (1 - 2/3): ', validate_math)
    assert str(step.calculated_result) == (validation)
