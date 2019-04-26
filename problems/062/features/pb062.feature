Feature: 给定一个 m x n 的矩形，计算可能的路径数
   一个机器人位于一个 m x n 网格的左上角
   机器人每次只能向下或者向右移动一步
   机器人试图达到网格的右下角
   
    Scenario: Case 1
        Given 输入 m = 3
        And 输入 n = 2
        When 计算计算路径可能数量
        Then 得到结果 3

    Scenario: Case 2
        Given 输入 m = 7
        And 输入 n = 3
        When 计算计算路径可能数量
        Then 得到结果 28