from behave import given, when, then, step
from  pb115 import Solution

@given(u'输入 S = "{string_s}"')
def step_impl(step, string_s):
    step.string_s = (string_s)

@given(u'输入 T = "{string_t}"')
def step_impl(step, string_t):
    step.string_t = (string_t)

@when(u'计算一个字符串的子序列')
def step_impl(step):  
    calKit = Solution()
    step.calculated_result =  calKit.numDistinct(step.string_s, step.string_t)  

@then(u'得到结果 {number:d}')
def step_impl(step, number):
    assert step.calculated_result == number
