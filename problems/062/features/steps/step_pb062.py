from behave import given, when, then, step
from  pb062 import Solution

@given(u'输入 m = {m:d}')
def step_impl(step, m):
    step.m = m

@given(u'输入 n = {n:d}')
def step_impl(step, n):
    step.n = n

@when(u'计算计算路径可能数量')
def step_impl(step):  
    calKit = Solution()
    step.calculated_result =  calKit.uniquePaths(step.m, step.n)  

@then(u'得到结果 {number:d}')
def step_impl(step, number):
    print(number)
    assert step.calculated_result == number
