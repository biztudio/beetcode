Feature: 计算一个字符串的子序列
   一个字符串的一个子序列是指通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
   （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
   
    Scenario: Case 1
        Given 输入 S = "rabbbit"
        And 输入 T = "rabbit"
        When 计算一个字符串的子序列
        Then 得到结果 3

    Scenario: Case 2
        Given 输入 S = "babgbag"
        And 输入 T = "bag"
        When 计算一个字符串的子序列
        Then 得到结果 5    