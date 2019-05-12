from behave import given, when, then, step
from  pb679 import Solution

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
    assert str(step.calculated_result) == (validation)
