from behave import given, when, then, step
from  pb121 import Solution

@given(u'Input {prices_string}')
def step_impl(step, prices_string):
    step.prices_string = (prices_string)

@when(u'Calculate')
def step_impl(step):  
    calKit = Solution()
    prices = [int(c) for c in step.prices_string.split(",")]
    step.calculated_result =  calKit.maxProfit(prices)  

@then(u'Get Result {number:d}')
def step_impl(step, number):
    assert step.calculated_result == number
