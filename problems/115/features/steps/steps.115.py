from behave import given, when, then, step

@given('输入: S = "(.*)"')
def have_the_string_s(step, string_s):
    print(string_s)
    pass

@given('输入: T = "(.*)"')
def have_the_string_t(step, string_t):
    print(string_t)
    pass

@when('计算一个字符串的子序列')
def step_when(context):  
    pass    

@then('得到结果 (\d+)')
def get_the_result(step, expected):
    '''得到结果 (\d+)'''
    expected = int(expected)
    assert 3 == expected#, \
       # "Got %d" % world.number
