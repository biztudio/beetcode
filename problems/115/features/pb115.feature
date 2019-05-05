Feature: 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数
   一个字符串的一个子序列是指通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
   （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
   
    Scenario: 1 个字符子序列 001
        Given 输入 S = "ababgbag"
        And 输入 T = "b"
        When 计算一个字符串的子序列
        Then 得到结果 3  

    Scenario: 1 个字符子序列 002
        Given 输入 S = "ababgbag"
        And 输入 T = "g"
        When 计算一个字符串的子序列
        Then 得到结果 2      

    Scenario: 2 个字符子序列 001
        Given 输入 S = "rabbbit"
        And 输入 T = "bb"
        When 计算一个字符串的子序列
        Then 得到结果 3 

    Scenario: 2 个字符子序列 002
        Given 输入 S = "rabbbit"
        And 输入 T = "ab"
        When 计算一个字符串的子序列
        Then 得到结果 3    

    Scenario: 2 个字符子序列 003
        Given 输入 S = "ababgbag"
        And 输入 T = "ag"
        When 计算一个字符串的子序列
        Then 得到结果 5

    Scenario: 2 个字符子序列 004
        Given 输入 S = "ddd"
        And 输入 T = "dd"
        When 计算一个字符串的子序列
        Then 得到结果 3        

    Scenario: 2 个字符子序列 005
        Given 输入 S = "dd"
        And 输入 T = "dd"
        When 计算一个字符串的子序列
        Then 得到结果 1                   

    Scenario: 3 个字符子序列 001
        Given 输入 S = "ababgbag"
        And 输入 T = "bag"
        When 计算一个字符串的子序列
        Then 得到结果 5        

    Scenario: 3 个字符子序列 002
        Given 输入 S = "rabbbit"
        And 输入 T = "bbb"
        When 计算一个字符串的子序列
        Then 得到结果 1    

     Scenario: 4 个字符子序列 001
        Given 输入 S = "rabbbit"
        And 输入 T = "abit"
        When 计算一个字符串的子序列
        Then 得到结果 3            

    Scenario: 5 个字符子序列 001
        Given 输入 S = "rabbbit"
        And 输入 T = "rabit"
        When 计算一个字符串的子序列
        Then 得到结果 3  

    Scenario: 6 个字符子序列 001
        Given 输入 S = "rabbbit"
        And 输入 T = "rabbit"
        When 计算一个字符串的子序列
        Then 得到结果 3      