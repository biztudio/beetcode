from behave import given, when, then, step
from  pb300 import Solution

@given(u'输入 "{nums}"')
def step_impl(step, nums):
    step.nums = (nums)

@when(u'计算最长上升子序列的长度')
def step_impl(step):  
    calKit = Solution()
    step.calculated_result =  calKit.lengthOfLIS(step.nums)  

@then(u'得到结果 {number:d}')
def step_impl(step, number):
    assert step.calculated_result == number
